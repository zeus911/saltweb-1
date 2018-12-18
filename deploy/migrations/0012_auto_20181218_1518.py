# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 07:18
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0011_auto_20181218_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='jids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.CharField(max_length=255, unique=True)),
                ('load', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/RADWEmflQDHyXLLaVdg4FXNXDSgQbQbVCsLhMMVrgQPd9xMAWxbPyq9KUUnP5JNMmpbC5kkNsbyYctrP', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
