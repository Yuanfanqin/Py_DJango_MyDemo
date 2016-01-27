# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100, null=True)),
                ('subscribes', models.CommaSeparatedIntegerField(default='', max_length=200)),
                ('friends', models.CommaSeparatedIntegerField(default='', max_length=200)),
                ('token', models.CharField(default='', max_length=100)),
                ('expire', models.BigIntegerField(default=86400)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.IntegerField(default=0)),
                ('g', models.IntegerField(default=0)),
                ('b', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo2.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryId', models.IntegerField()),
                ('name', models.CharField(default='', max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('equip', models.BooleanField(default=0)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo2.Color')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile', models.CharField(default='', max_length=30)),
                ('name', models.CharField(default='', max_length=100, unique=True)),
                ('photoUrl', models.CharField(default='', max_length=500)),
                ('auth_status', models.IntegerField(default=0)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo2.Role')),
                ('skills', models.ManyToManyField(to='Demo2.Skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
