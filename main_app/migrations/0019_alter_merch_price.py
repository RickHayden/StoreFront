# Generated by Django 4.1.2 on 2022-10-17 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_merch_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merch',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
