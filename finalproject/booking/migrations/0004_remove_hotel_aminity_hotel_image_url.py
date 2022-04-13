# Generated by Django 4.0.3 on 2022-03-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='aminity',
        ),
        migrations.AddField(
            model_name='hotel',
            name='image_url',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
