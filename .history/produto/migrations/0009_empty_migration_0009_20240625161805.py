from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion Generated by Django 4.2.11 on 2024-06-25 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_pedido_itempedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(max_length=50, default='Pendente'),
        ),
    ]
