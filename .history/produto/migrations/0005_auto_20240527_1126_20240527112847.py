# Generated by Django 4.2.11 on 2024-05-27 14:26

from django.db import migrations


class Migration(migrations.Migration):
migrations.AddField(
    model_name='produto',
    name='preco_marketing',
    field=models.FloatField(verbose_name='Preço de Marketing'),
),
    dependencies = [
        ('produto', '0004_alter_variacao_preco_marketing_promocional'),
    ]

    operations = [
    ]
