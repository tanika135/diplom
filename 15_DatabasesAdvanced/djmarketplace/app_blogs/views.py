# from app_blogs.utils import reduce_user_balance, publish_post
# from django.db import transaction

from django.shortcuts import render
from app_blogs.models import Post
import logging


logger = logging.getLogger(__name__)


def post_list(request):
    posts = Post.objects.select_related('blog').only('title', 'blog__name').order_by('blog').all()
    logger.info('Запрошена страница со списком записей блогов')
    return render(request, 'app_blogs/posts_list.html', {'posts_list': posts})


# @transaction.atomic
# def publish_blog_post(post_id, user_id, scope_value):
#     """Использование atomic как менеджер контекста"""
#     with transaction.atomic():
#         reduce_user_balance(user_id, scope_value)
#         publish_post(post_id)
