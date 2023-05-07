# from django.db import transaction
# from app_blogs.utils import reduce_user_balance, publish_post
from django.shortcuts import render



#@transaction.atomic
# def publish_blog_post(post_id, user_id, scope_value):
#     """Использование atomic как менеджер контекста"""
#     with transaction.atomic():
#         reduce_user_balance(user_id, scope_value)
#         publish_post(post_id)


