# Generated by Django 3.1.7 on 2021-04-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clocksystem',
            name='clocked_out_at',
            field=models.TimeField(null=True),
        ),
    ]
