# Generated by Django 3.0 on 2021-01-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0005_auto_20210106_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='customerLocation',
            field=models.BooleanField(default=False),
        ),
    ]