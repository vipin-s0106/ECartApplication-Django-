# Generated by Django 2.1.3 on 2019-01-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20190117_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='date',
            field=models.CharField(default='2019-01-19', max_length=15),
        ),
    ]
