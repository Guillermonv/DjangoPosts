# Generated by Django 3.0.3 on 2020-03-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='no-video', null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
