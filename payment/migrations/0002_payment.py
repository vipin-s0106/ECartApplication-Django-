# Generated by Django 2.1.3 on 2019-02-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
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
    ]
