# Generated by Django 3.2 on 2023-06-09 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats_sale', '0008_auto_20230609_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='object',
            old_name='name',
            new_name='object_name',
        ),
        migrations.AddField(
            model_name='category',
            name='object_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flats_sale.object', verbose_name='Объект'),
            preserve_default=False,
        ),
    ]