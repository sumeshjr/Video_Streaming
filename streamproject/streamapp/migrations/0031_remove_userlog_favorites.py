# Generated by Django 4.1.7 on 2023-05-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0030_rename_fav_userlog_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlog',
            name='favorites',
        ),
    ]
