# Generated by Django 4.1.2 on 2022-10-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='title',
            field=models.CharField(default='Wishlist', max_length=150),
        ),
    ]
