# Generated by Django 2.1.4 on 2019-02-09 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercart', '0005_auto_20190207_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='orderitem',
        ),
        migrations.RemoveField(
            model_name='myorder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='myorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyOrder',
        ),
    ]
