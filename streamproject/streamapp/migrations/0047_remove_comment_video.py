# Generated by Django 4.1.7 on 2023-05-24 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0046_alter_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='video',
        ),
    ]
