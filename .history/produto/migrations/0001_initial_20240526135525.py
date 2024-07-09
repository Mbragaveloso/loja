# Generated by Django 4.2.11 on 2024-05-26 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tipo', models.CharField(choices=[('P', 'Produto'), ('V', 'Variacao')], max_length=1)),
                ('slug', models.SlugField(unique=True)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField(max_length=800)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto/imagens/')),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('GG', 'Extra Grande')], max_length=2)),
                ('preco_marketing', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('preco_marketing_promocional', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço Promo.')),
            ],
        ),
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=50)),
                ('preco_marketing', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('preco_marketing_promocional', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estoque', models.PositiveIntegerField(default=1)),
                ('descricao', models.CharField(blank=True, max_length=50, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'verbose_name': 'Variação',
                'verbose_name_plural': 'Variações',
            },
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produtos',
            field=models.ManyToManyField(through='produto.ItemCarrinho', to='produto.produto'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
