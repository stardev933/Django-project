# Generated by Django 3.2.10 on 2021-12-20 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0009_alter_helprequest_accepted_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='helprequest',
            old_name='text_content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='helprequestoffer',
            old_name='text_content',
            new_name='text',
        ),
    ]
