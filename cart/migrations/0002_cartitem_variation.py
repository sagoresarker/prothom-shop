# Generated by Django 4.2 on 2023-04-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]