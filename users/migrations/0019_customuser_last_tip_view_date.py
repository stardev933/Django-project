# Generated by Django 3.2.10 on 2022-01-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_rename_text_about_customuser_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_tip_view_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
