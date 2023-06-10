# Generated by Django 3.2 on 2023-06-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats_sale', '0006_delete_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('location', models.CharField(max_length=128, verbose_name='Расположение')),
            ],
        ),
    ]