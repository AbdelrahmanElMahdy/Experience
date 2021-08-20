from django.db import models
from django.contrib.auth.models import (AbstractUser,BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("you must provid email address")

        user=self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None):

        user=self.create_user(email=email,password=password)
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
    is_active=models.BooleanField(default=True)
    is_stuff=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects= UserManager()
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_module_perms(self, app_label):
       return self.is_admin
    def has_perm(self, perm, obj=None):
       return self.is_admin

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)