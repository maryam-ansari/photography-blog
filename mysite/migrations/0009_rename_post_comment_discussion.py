# Generated by Django 5.0.2 on 2024-04-07 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='discussion',
        ),
    ]
