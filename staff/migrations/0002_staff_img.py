# Generated by Django 3.2 on 2023-06-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='img',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d/', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
