# Generated by Django 2.1.3 on 2019-01-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usercart', '0002_auto_20190119_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_id', models.AutoField(default=1000, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=150)),
                ('transaction_amount', models.FloatField()),
                ('payment_status', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='myorder',
            name='order_date',
            field=models.CharField(default='2019-01-21', max_length=15),
        ),
        migrations.AddField(
            model_name='myorder',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usercart.Payment'),
        ),
    ]
