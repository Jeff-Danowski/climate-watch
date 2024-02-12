# Generated by Django 5.0.2 on 2024-02-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15)),
                ('temp', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('airquaility', models.IntegerField(default=0)),
            ],
        ),
    ]
