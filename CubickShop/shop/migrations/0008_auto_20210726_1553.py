# Generated by Django 3.2.5 on 2021-07-26 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210725_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
