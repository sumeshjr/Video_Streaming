# Generated by Django 4.1.7 on 2023-05-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0044_alter_video_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='favorite',
            new_name='fav',
        ),
    ]
