# Generated by Django 3.2 on 2023-06-12 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='flat',
        ),
    ]