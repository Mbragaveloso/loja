# Generated by Django 4.2.11 on 2024-05-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_remove_produto_preco_remove_variacao_preco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(verbose_name='Preço Promo.'),
        ),
    ]
