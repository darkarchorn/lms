# Generated by Django 4.1.2 on 2022-11-28 15:25

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_coursepost_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepost',
            name='image_url',
            field=models.FileField(blank=True, null=True, upload_to=courses.models.upload_to),
        ),
    ]
