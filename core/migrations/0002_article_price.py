# Generated by Django 4.0.4 on 2022-06-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
