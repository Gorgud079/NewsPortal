import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed, post_save, pre_save, pre_init
from django.dispatch import receiver
from .models import Post, User, Subscribe
from dotenv import load_dotenv
import os

load_dotenv()


@receiver(m2m_changed, sender=Post.categories.through)
def new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'pre_add':
        subject = f'Новая статья'
        html_content = render_to_string('email_attention.html', {
            'news': instance
        })
        for id in kwargs['pk_set']:
            cat_id = id
        list_of_sub = Subscribe.objects.filter(category_current=cat_id).values('user_current')
        sub = []

        for i in list_of_sub:
            user_email = User.objects.get(id=i['user_current']).email
            sub.append(user_email)

        msg = EmailMultiAlternatives(
            subject=subject,
            body=instance.headline,
            from_email=f'{os.getenv("EMAIL_HOST_USER")}@yandex.ru',
            to=sub
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()