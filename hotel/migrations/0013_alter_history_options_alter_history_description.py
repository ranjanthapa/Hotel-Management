# Generated by Django 5.0.1 on 2024-02-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_history_visionandgoal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name_plural': 'History'},
        ),
        migrations.AlterField(
            model_name='history',
            name='description',
            field=models.TextField(),
        ),
    ]
