# Generated by Django 3.0.3 on 2020-03-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200323_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='no-photo', null=True, upload_to='posts/photos'),
        ),
    ]
