# Generated by Django 3.2 on 2023-06-09 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats_sale', '0009_auto_20230609_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='name',
        ),
        migrations.AddField(
            model_name='flat',
            name='object_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flats_sale.object', verbose_name='Объект'),
            preserve_default=False,
        ),
    ]
