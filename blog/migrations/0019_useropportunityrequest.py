# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 03:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_auto_20170921_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOpportunityRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.ManyToManyField(to='blog.Code')),
                ('keyword', models.ManyToManyField(to='blog.Keyword')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Opportunities Requests',
            },
        ),
    ]
