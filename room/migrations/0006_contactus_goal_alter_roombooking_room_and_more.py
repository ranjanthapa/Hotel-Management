# Generated by Django 5.0.1 on 2024-01-17 15:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_rename_type_roomdetail_room_type_roombooking_adults_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be 10 digits long.', regex='^\\d{10}$')])),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_vision', models.CharField(max_length=100)),
                ('mission', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='room',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
        migrations.CreateModel(
            name='ReviewAndRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('goal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.goal')),
                ('user_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.reviewandrating')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images/room_image')),
                ('image2', models.ImageField(upload_to='images/room_image')),
                ('image3', models.ImageField(upload_to='images/room_image')),
                ('image4', models.ImageField(upload_to='images/room_image')),
                ('image5', models.ImageField(upload_to='images/room_image')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
        migrations.AddField(
            model_name='roomdetail',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='room.roomimage'),
        ),
    ]