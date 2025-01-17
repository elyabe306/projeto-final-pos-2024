# Generated by Django 5.1.5 on 2025-01-15 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address_street', models.CharField(max_length=100)),
                ('address_suite', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=100)),
                ('address_zipcode', models.CharField(max_length=10)),
                ('address_lat', models.FloatField()),
                ('address_lng', models.FloatField()),
                ('phone', models.CharField(max_length=11)),
                ('website', models.URLField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_catchphrase', models.CharField(max_length=100)),
                ('company_bs', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
                ('thumbnailUrl', models.URLField(blank=True)),
                ('albumId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.albums')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.posts')),
            ],
        ),
        migrations.CreateModel(
            name='todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
        migrations.AddField(
            model_name='albums',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]
