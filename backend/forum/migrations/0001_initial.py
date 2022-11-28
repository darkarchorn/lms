# Generated by Django 4.1.2 on 2022-11-28 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, max_length=500)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
