# Generated by Django 3.2.5 on 2021-08-14 14:32

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210812_1424'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'В работе'), ('published', 'Опубликована')], default='draft', max_length=10, verbose_name='Статус'),
        ),
    ]
