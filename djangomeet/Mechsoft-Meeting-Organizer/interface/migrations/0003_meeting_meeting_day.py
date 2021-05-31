# Generated by Django 3.2.3 on 2021-05-30 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_rename_link_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_day',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
