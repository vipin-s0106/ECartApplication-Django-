# Generated by Django 2.1.3 on 2019-01-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20190117_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='review_image2',
            field=models.ImageField(default='http://dummyimage.com/60x60/666/ffffff&text=No+Image', upload_to='', verbose_name='Attach image'),
        ),
    ]
