# Generated by Django 4.1.2 on 2022-10-16 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_wishlist_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='content',
            new_name='merchs',
        ),
    ]
