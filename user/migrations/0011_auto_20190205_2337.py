# Generated by Django 2.1.3 on 2019-02-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190113_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state_choice',
            field=models.CharField(choices=[('', '--Select--'), ('Maharashtra', 'Mahashtra'), ('Rajsthan', 'Rajsthan'), ('Gujrat', 'Gujrat'), ('Karnataka', 'Karnataka'), ('Delhi', 'Delhi')], default='', max_length=11, verbose_name='State'),
        ),
    ]
