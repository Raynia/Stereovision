# Generated by Django 3.1.2 on 2020-11-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stereovision', '0002_auto_20201113_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_index', models.PositiveIntegerField()),
            ],
        ),
    ]