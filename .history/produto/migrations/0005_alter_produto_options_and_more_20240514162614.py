# Generated by Django 4.2.11 on 2024-05-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20240513_2324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='descricao',
            new_name='descricao_curta',
             field=models.TextField(default='', max_length=255),
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao_curta',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(default='', verbose_name='Preço'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavel'), ('S', 'Simples')], default='V', max_length=1),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]