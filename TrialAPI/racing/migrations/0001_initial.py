# Generated by Django 3.1.7 on 2021-11-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=30)),
                ('car_brand', models.CharField(max_length=20)),
                ('round_finishing_time', models.IntegerField(default=0)),
            ],
        ),
    ]
