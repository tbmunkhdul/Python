# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20161228_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
