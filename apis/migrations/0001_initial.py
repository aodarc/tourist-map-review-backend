# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(db_index=True, default=49.836085, verbose_name='lat')),
                ('lon', models.FloatField(db_index=True, default=24.005691, verbose_name='lon')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Заголовок')),
                ('description', models.TextField(default='Some Description', max_length=300, verbose_name='Короткий опис')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст статті')),
                ('title_image', models.ImageField(blank=True, default='./reviews/images/maps.png', upload_to='./reviews/images', verbose_name='Головне зоображення')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.TextField(blank=True, help_text='Facebook token for offline access', null=True)),
                ('facebook_name', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_profile_url', models.TextField(blank=True, null=True)),
                ('website_url', models.TextField(blank=True, null=True)),
                ('blog_url', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
