# Generated by Django 4.2.11 on 2024-06-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
