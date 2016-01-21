# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Demo1', '0003_auto_20160121_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo1.User'),
        ),
        migrations.AlterField(
            model_name='role',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo1.Color'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo1.Color'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demo1.Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(null=True, to='Demo1.Skill'),
        ),
    ]
