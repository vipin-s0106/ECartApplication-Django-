# Generated by Django 2.1.4 on 2019-01-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20190113_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='product_image1',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='product_image2',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
