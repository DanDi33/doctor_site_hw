# Generated by Django 5.0.6 on 2024-06-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0003_ed_and_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ed_and_work',
            name='diplom_img',
            field=models.ImageField(blank=True, null=True, upload_to='Ed_and_work_img'),
        ),
    ]