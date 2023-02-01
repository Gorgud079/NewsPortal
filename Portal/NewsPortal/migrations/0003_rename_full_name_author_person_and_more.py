# Generated by Django 4.1.5 on 2023-02-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0002_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='full_name',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='count_rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rating_dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rating_like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating_dislike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating_like',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='post_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(max_length=255),
        ),
    ]
