# Generated by Django 3.2.8 on 2022-01-15 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]