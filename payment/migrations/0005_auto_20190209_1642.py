# Generated by Django 2.1.4 on 2019-02-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20190207_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='deliver_date',
            field=models.CharField(default='2019-02-16', max_length=15),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_date',
            field=models.CharField(default='2019-02-09', max_length=15),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
