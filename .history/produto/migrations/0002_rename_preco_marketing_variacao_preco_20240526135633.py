# Generated by Django 4.2.11 on 2024-05-26 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variacao',
            old_name='preco_marketing',
            new_name='preco',
        ),
    ]
