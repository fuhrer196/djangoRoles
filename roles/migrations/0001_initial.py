# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleName', models.CharField(max_length=15)),
                ('aff', models.CharField(max_length=15, choices=[(b'T', b'Town'), (b'M', b'Mafia')])),
                ('meetingGroup', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='roleAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('role', models.ForeignKey(to='roles.role')),
            ],
        ),
        migrations.CreateModel(
            name='setup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('setupName', models.CharField(max_length=15)),
                ('roles', models.ManyToManyField(to='roles.role', through='roles.roleAdd')),
            ],
        ),
        migrations.AddField(
            model_name='roleadd',
            name='setup',
            field=models.ForeignKey(to='roles.setup'),
        ),
    ]
