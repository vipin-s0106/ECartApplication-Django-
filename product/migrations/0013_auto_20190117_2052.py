# Generated by Django 2.1.3 on 2019-01-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20190116_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='date',
            field=models.CharField(default='2019-01-17', max_length=15),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
