# Generated by Django 5.0.1 on 2024-02-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("room", "0008_menucategory_alter_aboutus_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenitie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="roomdetail",
            name="amenities",
        ),
        migrations.AddField(
            model_name="roomdetail",
            name="amenities",
            field=models.ManyToManyField(related_name="rooms", to="room.amenitie"),
        ),
    ]