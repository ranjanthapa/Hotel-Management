# Generated by Django 5.0.1 on 2024-01-10 02:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('single', 'Single'), ('family', 'Family'), ('deluxe', 'Deluxe'), ('president', 'President')], max_length=30)),
                ('availability', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('clean', 'Clean'), ('maintenance', 'Maintenance'), ('dirty', 'Dirty')], max_length=50)),
                ('amenities', models.CharField(max_length=100)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
    ]
