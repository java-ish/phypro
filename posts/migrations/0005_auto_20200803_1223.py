# Generated by Django 3.0.8 on 2020-08-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='done',
            new_name='answer_status',
        ),
    ]
