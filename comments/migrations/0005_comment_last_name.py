# Generated by Django 3.0.3 on 2020-03-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20200314_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
