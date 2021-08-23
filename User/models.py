from django.db import models
from django.contrib.auth.models import (AbstractUser,BaseUserManager)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("you must provid email address")

        if not username:
            raise ValueError("you must provid username")

        user=self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.username=username
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email,username, password=None):

        user=self.create_user(email=email, username=username, password=password)
        user.is_admin=True
        user.is_stuff=True        
        user.save(using=self._db)
        
        return user


class User(AbstractUser):
    email=models.EmailField(
        verbose_name='Email Address',
        max_length=254,
        unique=True
    )

    username=models.CharField(
        verbose_name="Username",
        max_length=50,
        unique=True,
        blank=False
    )
    
    first_name=models.CharField(
        verbose_name="first name",
        max_length=50,
        blank=True
    )
    last_name=models.CharField(
        verbose_name="last name",
        max_length=50,
        blank=True
    )
    date_created=models.DateField(
        verbose_name="Date Created",
        auto_now=True, 
        auto_now_add=False)

    is_active=models.BooleanField(default=True)
    is_stuff=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verified=models.BooleanField(verbose_name="is verified",default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects= UserManager()
    @property
    def is_staff(self):
        return self.is_admin
    
    def verify(self):
        self.is_verified=True
    
    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
       return self.is_admin
    def has_perm(self, perm, obj=None):
       return self.is_admin

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)