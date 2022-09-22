# from django.db.models.signals import pre_save, post_save
# from django.contrib.auth.models import User


# from .models import *


# def updateUser(sender, instance, **kwargs):
#     user = instance
#     if user.email != '':
#         user.username = user.email
#     print('email set as username')


# pre_save.connect(updateUser, sender=User)
