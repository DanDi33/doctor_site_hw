# Generated by Django 5.0.6 on 2024-08-15 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logmessage',
            name='user',
        ),
    ]