# Generated by Django 3.0.7 on 2020-06-19 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200618_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date ordered'),
        ),
    ]
