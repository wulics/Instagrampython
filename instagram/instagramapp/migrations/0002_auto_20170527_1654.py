# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miusuario',
            old_name='user',
            new_name='usuario',
        ),
    ]