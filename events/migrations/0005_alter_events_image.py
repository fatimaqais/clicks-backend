# Generated by Django 3.2.20 on 2023-11-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_events_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
