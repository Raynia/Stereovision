# Generated by Django 3.1.2 on 2020-11-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stereovision', '0003_auto_20201116_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetimage',
            name='target_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]