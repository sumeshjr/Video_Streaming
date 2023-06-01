# Generated by Django 4.1.7 on 2023-05-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0013_remove_video_liked_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='recent_update_images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
