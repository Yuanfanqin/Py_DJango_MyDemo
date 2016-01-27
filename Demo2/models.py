from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
import json
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Color(models.Model):
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)


class Skill(models.Model):
    categoryId = models.IntegerField()
    name = models.CharField(default="", max_length=100)
    level = models.IntegerField(default=0)
    color = models.ForeignKey(Color, null=True)
    equip = models.BooleanField(default=0)


class Role(models.Model):
    name = models.CharField(default="", max_length=100)
    color = models.ForeignKey(Color, null=True)


# class UserManager(models.Manager):
#     def get_by_natural_key(self, mobile, name, photoUrl, auth_status):
#         return self.get(mobile=mobile, name=name, photoUrl=photoUrl, auth_status=auth_status)


class User(AbstractBaseUser):
    # objects = UserManager()
    mobile = models.CharField(max_length=30, default="")
    name = models.CharField(max_length=100,  unique=True, default="")
    photoUrl = models.CharField(max_length=500, default="")
    auth_status = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill)
    role = models.ForeignKey(Role, null=True)

    USERNAME_FIELD = 'name'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        t = Token.objects.create(user=instance)


class Account(models.Model):
    user = models.ForeignKey(User, null=True, related_name='accounts')
    password = models.CharField(max_length=100, null=True)
    subscribes = models.CommaSeparatedIntegerField(max_length=200, default="")
    friends = models.CommaSeparatedIntegerField(max_length=200, default="")
    token = models.CharField(max_length=100, default="")
    expire = models.BigIntegerField(default=60*60*24)