# Generated by Django 3.2.8 on 2022-01-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_stuassign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuassign',
            name='Sfile',
            field=models.FileField(upload_to='submissions'),
        ),
    ]