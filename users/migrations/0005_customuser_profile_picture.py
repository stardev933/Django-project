# Generated by Django 3.2.6 on 2021-11-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_kcalamount_amount_gt_0'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
