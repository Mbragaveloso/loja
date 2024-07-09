from django.db import migrations, models

def add_descricao_field(apps, schema_editor):
    Produto = apps.get_model('produto', 'Produto')
    db_alias = schema_editor.connection.alias
    Produto.objects.using(db_alias).add_to_class(
        'descricao',
        models.TextField(default='')
    )

class Migration(migrations.Migration):

    dependencies = [
        ('produto', 'XXXX_migration_name_here'),
    ]

    operations = [
        migrations.RunPython(add_descricao_field),
    ]