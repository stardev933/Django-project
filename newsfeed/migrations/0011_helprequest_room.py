# Generated by Django 3.2.9 on 2022-01-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_dm_room'),
        ('newsfeed', '0010_auto_20211220_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_request_set', to='core.roomdm'),
        ),
    ]
