# Generated by Django 2.1 on 2020-02-15 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='datecreated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
