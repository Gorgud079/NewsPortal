from django.db import models
from django.contrib.auth.models import User
from .example import POSITIONS, news


class Author(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.user_rate = 0
        for post in Post.objects.filter(author=self.person):
            self.user_rate += post.post_rating * 3
            for comment in Comment.objects.filter(posts=post):
                self.user_rate += comment.comment_rating
        for comment in Comment.objects.filter(users=self.person):
            self.user_rate += comment.comment_rating
        self.save()

    def __str__(self):
        return f'{self.person.username}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)

    position = models.CharField(max_length=2, choices=POSITIONS, default=news)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through="PostCategory")

    def like_post(self, amount=1):
        self.post_rating += amount
        self.save()

    def dislike_post(self, amount=1):
        self.post_rating -= amount
        self.save()

    def preview(self):
        self.content = self.content[0:125] + '...'
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_rating = models.IntegerField(default=0)

    def like_comment(self, amount=1):
        self.comment_rating += amount
        self.save()

    def dislike_comment(self, amount=1):
        self.comment_rating -= amount
        self.save()