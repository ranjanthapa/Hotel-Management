# Generated by Django 5.0.1 on 2024-02-12 13:31

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_description',
            field=tinymce.models.HTMLField(),
        ),
    ]