# Generated by Django 4.1.2 on 2022-11-28 05:38

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepost',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=courses.models.upload_to),
        ),
    ]
