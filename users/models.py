from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **kwargs):
        if email is None:
            raise TypeError(_('Users should have an email address.'))
        if first_name is None:
            raise TypeError(_('Users should have a first name'))
        if last_name is None:
            raise TypeError(_('Users should have a last name'))
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **kwargs)
        if password is None:
            raise ValueError(_('Password should not be none'))
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, first_name, last_name, password, **kwargs)
        
        user.save()
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    
    
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["first_name", "last_name"]
    


    def __str__(self):
        return self.email
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
