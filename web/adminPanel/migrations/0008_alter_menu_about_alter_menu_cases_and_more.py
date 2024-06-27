# Generated by Django 5.0.6 on 2024-06-27 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0007_rename_feedbackes_menu_feedbacks_alter_case_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='about',
            field=models.CharField(default='О себе', max_length=100, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='cases',
            field=models.CharField(default='Кейсы', max_length=100, verbose_name='Кейсы'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ed_and_work',
            field=models.CharField(default='Образование и работа', max_length=100, verbose_name='Образование и работа'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='feedbacks',
            field=models.CharField(default='Отзывы', max_length=100, verbose_name='Отзывы'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='services',
            field=models.CharField(default='Услуги', max_length=100, verbose_name='Услуги'),
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
                ('price', models.IntegerField(verbose_name='Цена')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Service_img', verbose_name='Изображение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
