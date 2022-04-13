# Generated by Django 4.0.3 on 2022-04-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='facilities', to='booking.facilities'),
        ),
    ]
