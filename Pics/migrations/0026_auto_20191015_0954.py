# Generated by Django 2.2 on 2019-10-15 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0025_remove_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]