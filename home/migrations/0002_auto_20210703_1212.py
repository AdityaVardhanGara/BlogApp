# Generated by Django 3.1.7 on 2021-07-03 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timeStamp',
            new_name='dateTime',
        ),
    ]
