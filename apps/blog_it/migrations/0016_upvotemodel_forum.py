# Generated by Django 3.2.10 on 2022-07-16 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_forummodel_view_count'),
        ('blog_it', '0015_remove_upvotemodel_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='upvotemodel',
            name='forum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_blog', to='forum.forummodel'),
        ),
    ]