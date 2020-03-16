# Generated by Django 3.0.4 on 2020-03-15 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_comments'),
        ('comments', '0002_auto_20200314_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='posts.Post'),
        ),
    ]