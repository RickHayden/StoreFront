# Generated by Django 4.1.2 on 2022-10-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_merch_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merch',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
