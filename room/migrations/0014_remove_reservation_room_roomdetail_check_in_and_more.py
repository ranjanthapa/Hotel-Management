# Generated by Django 5.0.1 on 2024-01-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_alter_roomdetail_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='room',
        ),
        migrations.AddField(
            model_name='roomdetail',
            name='check_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomdetail',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]
