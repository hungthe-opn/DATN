# Generated by Django 3.2.10 on 2022-09-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0002_notificationmodel_to_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='is_upvote',
            field=models.BooleanField(default=False),
        ),
    ]
