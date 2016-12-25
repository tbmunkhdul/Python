# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161221_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catergories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Catergories'),
        ),
    ]
