# Generated by Django 5.0.2 on 2024-04-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
