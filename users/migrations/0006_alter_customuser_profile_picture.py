# Generated by Django 3.2.6 on 2021-11-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='defaults/users/default_profile_pic.jpg', upload_to='users/profile_pics'),
        ),
    ]
