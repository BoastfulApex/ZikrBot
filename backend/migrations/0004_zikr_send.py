# Generated by Django 4.0.6 on 2022-07-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_zikr_zikr_arabic_zikr_zikr_mean'),
    ]

    operations = [
        migrations.AddField(
            model_name='zikr',
            name='send',
            field=models.BooleanField(default=False),
        ),
    ]
