# Generated by Django 3.0.8 on 2020-08-03 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200803_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tit',
        ),
        migrations.AddField(
            model_name='post',
            name='answer_status',
            field=models.BooleanField(default=False),
        ),
    ]
