# Generated by Django 4.1.7 on 2023-05-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0020_remove_userreg_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
