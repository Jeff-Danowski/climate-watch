# Generated by Django 5.0.2 on 2024-02-15 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airreport', '0009_alter_sensor_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 18, 37, 17, 722903)),
        ),
    ]
