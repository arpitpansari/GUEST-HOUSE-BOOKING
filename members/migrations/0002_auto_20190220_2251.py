# Generated by Django 2.1.5 on 2019-02-20 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formsubmit',
            old_name='userbookings',
            new_name='user',
        ),
    ]
