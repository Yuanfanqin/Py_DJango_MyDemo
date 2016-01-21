from django.db import models
import json


# Create your models here.
class Color(models.Model):
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)


class Skill(models.Model):
    categoryId = models.IntegerField()
    name = models.CharField(default="",max_length=100)
    level = models.IntegerField(default=0)
    color = models.ForeignKey(Color,null=True)
    equip = models.BooleanField(default=0)


class Role(models.Model):
    name = models.CharField(default="",max_length=100)
    color = models.ForeignKey(Color,null=True)


class User(models.Model):
    mobile = models.CharField(max_length=30,default="")
    name = models.CharField(max_length=100,default="")
    photoUrl = models.CharField(max_length=500,default="")
    auth_status = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill,null=True)
    role = models.ForeignKey(Role,null=True)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),models.Model):
                d[attr] = json.loads(getattr(self, attr).toJSON())
            else:
                d[attr] = getattr(self, attr)
        print(d)
        return json.dumps(d)


class Account(models.Model):
    user = models.ForeignKey(User,null=True)
    subscribes = models.CommaSeparatedIntegerField(max_length=200,default="")
    friends = models.CommaSeparatedIntegerField(max_length=200,default="")
    token = models.CharField(max_length=100,default="")
    expire = models.BigIntegerField()

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),models.Model):
                d[attr] = json.loads(getattr(self, attr).toJSON())
            else:
                d[attr] = getattr(self, attr)
        print(d)
        return json.dumps(d)