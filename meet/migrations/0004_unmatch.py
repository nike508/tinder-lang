# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 02:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0003_auto_20160606_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unmatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='unmatch timestamp')),
                ('users', models.ManyToManyField(related_name='unmatches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
