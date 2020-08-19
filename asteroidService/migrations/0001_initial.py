# Generated by Django 3.1 on 2020-08-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asteroid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.CharField(default='1x1', max_length=5)),
                ('matrix', models.BinaryField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsteroidSighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('time', models.TimeField(blank=True, default=None, null=True)),
                ('observatory_code', models.CharField(default='ob_0000000', max_length=10)),
                ('device_code', models.CharField(default='de_00000', max_length=8)),
                ('device_resolution', models.CharField(default='1x1', max_length=5)),
                ('device_matrix', models.BinaryField(blank=True, default=None, null=True)),
                ('asteroid_code', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
