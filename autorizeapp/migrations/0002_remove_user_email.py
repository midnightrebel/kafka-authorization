# Generated by Django 4.0.6 on 2022-07-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autorizeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
