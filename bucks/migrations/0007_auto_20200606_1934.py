# Generated by Django 3.0.7 on 2020-06-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucks', '0006_auto_20200606_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_community_code',
            name='generated_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='point',
            name='community_code',
            field=models.IntegerField(),
        ),
    ]
