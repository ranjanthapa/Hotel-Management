# Generated by Django 5.0.1 on 2024-02-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Food Category',
            },
        ),
        migrations.AlterModelOptions(
            name='hotelshortintro',
            options={'verbose_name': 'Welcome Introduction', 'verbose_name_plural': 'Welcome Introduction'},
        ),
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='hotel.foodcategory')),
            ],
        ),
    ]
