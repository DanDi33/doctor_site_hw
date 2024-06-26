# Generated by Django 5.0.6 on 2024-06-28 09:09

import adminPanel.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=200)),
                ('slogan', models.TextField(blank=True, null=True)),
                ('main_foto', models.ImageField(default='avatar.jpg', upload_to='About_main_foto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ed_and_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=adminPanel.models.current_year, verbose_name='Год')),
                ('desc', models.TextField()),
                ('diplom_img', models.ImageField(blank=True, null=True, upload_to='Ed_and_work_img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(default='Сообщения', max_length=100, verbose_name='Сообщения')),
                ('about', models.CharField(default='О себе', max_length=100, verbose_name='О себе')),
                ('services', models.CharField(default='Услуги', max_length=100, verbose_name='Услуги')),
                ('cases', models.CharField(default='Кейсы', max_length=100, verbose_name='Кейсы')),
                ('ed_and_work', models.CharField(default='Образование и работа', max_length=100, verbose_name='Образование и работа')),
                ('feedbacks', models.CharField(default='Отзывы', max_length=100, verbose_name='Отзывы')),
                ('contacts', models.CharField(default='Контакты', max_length=100, verbose_name='Контакты')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('completed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Получено')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
        migrations.CreateModel(
            name='Paralax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='fon.jpg', upload_to='paralax_img', verbose_name='Паралакс 1')),
                ('img2', models.ImageField(default='fon.jpg', upload_to='paralax_img', verbose_name='Паралакс 2')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Service_img', verbose_name='Изображение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
