# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 07:05
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0005_auto_20181218_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/AFSa68lVkQGFulKytfMg3qjlbBcgYWHCnyPmxwmqkmNTW3ngdeJrrQnxkrmv6PbrQswGmkYqrhlNLV7m', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
