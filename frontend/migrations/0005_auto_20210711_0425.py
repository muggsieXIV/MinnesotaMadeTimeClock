# Generated by Django 3.1.5 on 2021-07-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20210706_0345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clocksystem',
            options={'ordering': ('date_worked', 'clocked_in_at', 'clocked_out_at', 'employee', 'location', 'role', 'hours_worked', 'minutes_worked', 'seconds_worked', 'in_comment', 'out_comment')},
        ),
        migrations.RenameField(
            model_name='clocksystem',
            old_name='comment',
            new_name='in_comment',
        ),
        migrations.RenameField(
            model_name='clocksystem',
            old_name='minutes',
            new_name='minutes_worked',
        ),
        migrations.AddField(
            model_name='clocksystem',
            name='out_comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clocksystem',
            name='seconds_worked',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
