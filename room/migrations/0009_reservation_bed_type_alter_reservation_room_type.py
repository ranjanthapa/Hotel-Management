# Generated by Django 5.0.1 on 2024-01-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_reservation_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='bed_type',
            field=models.CharField(blank=True, choices=[('single_bed', 'Single Bed'), ('double_bed', 'Double Bed'), ('king_bed', 'King Bed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('family', 'Family'), ('deluxe', 'Deluxe'), ('president', 'President')], max_length=30),
        ),
    ]