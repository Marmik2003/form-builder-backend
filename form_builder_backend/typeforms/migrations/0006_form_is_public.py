# Generated by Django 3.2.12 on 2022-04-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeforms', '0005_field_multiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
