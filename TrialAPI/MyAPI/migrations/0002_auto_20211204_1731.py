# Generated by Django 3.1.7 on 2021-12-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_spec',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]