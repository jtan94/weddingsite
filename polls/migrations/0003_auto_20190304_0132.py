# Generated by Django 2.1.7 on 2019-03-04 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190303_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitedguest',
            name='dietary_restrictions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invitedguest',
            name='rsvp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='additional_guests',
            field=models.IntegerField(default=0),
        ),
    ]
