# Generated by Django 3.2.10 on 2022-09-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0003_notificationmodel_is_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='is_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationmodel',
            name='is_following',
            field=models.BooleanField(default=False),
        ),
    ]
