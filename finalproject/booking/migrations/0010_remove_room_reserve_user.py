# Generated by Django 4.0.3 on 2022-03-27 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_room_reserve_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_reserve',
            name='user',
        ),
    ]
