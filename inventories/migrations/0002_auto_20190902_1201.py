# Generated by Django 2.1.5 on 2019-09-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='is_empty',
            field=models.BooleanField(default=False),
        ),
    ]
