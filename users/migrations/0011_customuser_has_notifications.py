# Generated by Django 3.2.6 on 2021-11-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_notifications',
            field=models.BooleanField(default=False),
        ),
    ]
