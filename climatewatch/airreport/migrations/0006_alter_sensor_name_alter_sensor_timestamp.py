# Generated by Django 5.0.2 on 2024-02-15 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airreport', '0005_alter_sensor_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 18, 5, 8, 771996)),
        ),
    ]
