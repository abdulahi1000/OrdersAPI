from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken 

class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name,last_name,phone_number,password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User should have a email')
        
        user = self.model(username=username, last_name=last_name, first_name=first_name, phone_number=phone_number, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        
        user = self.create_user(username,email, password)
        user.is_superuser =True
        user.is_staff = True
        user.save()
        return user
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50, )
    phone_number = models.CharField(max_length=20,null=True )
    is_staff = models.BooleanField(default=False)
    pass

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def __str__(self):
        return self.email
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh': str(refresh),
            'access':str(refresh.access_token)
        }

