# Generated by Django 3.2 on 2021-06-01 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kala', '0006_checkout_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
