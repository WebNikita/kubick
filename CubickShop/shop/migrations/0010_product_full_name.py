# Generated by Django 3.2.6 on 2021-08-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Полное название товара'),
        ),
    ]
