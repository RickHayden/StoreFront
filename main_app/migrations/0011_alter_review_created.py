# Generated by Django 4.1.2 on 2022-10-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_review_created_review_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
