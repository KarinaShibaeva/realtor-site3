# Generated by Django 3.2 on 2023-06-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats_sale', '0003_category_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.AddField(
            model_name='flat',
            name='location',
            field=models.CharField(default=1, max_length=128, verbose_name='Расположение'),
            preserve_default=False,
        ),
    ]
