# Generated by Django 3.2.6 on 2022-06-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_slot_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
