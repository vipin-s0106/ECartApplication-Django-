# Generated by Django 2.1.3 on 2019-02-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20190202_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='date',
            field=models.CharField(default='2019-02-05', max_length=15),
        ),
    ]
