# Generated by Django 3.1.2 on 2020-10-28 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Posts', max_length=255),
        ),
    ]