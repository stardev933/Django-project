# Generated by Django 3.2.6 on 2021-12-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0006_auto_20211215_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='accept_date',
            field=models.DateTimeField(null=True),
        ),
    ]
