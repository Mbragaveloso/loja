from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1
    

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_marketing', 'preco_marketing_promocional')
    fields = ['nome', 'descricao_curta', 'preco_marketing', 'preco_marketing_promocional']
    readonly_fields = ['preco_formatado', 'preco_promocional_formatado']  # Atualize aqui
    
    def preco_formatado(self, obj):
        return obj.get_preco_formatado()  # Substitua pelo método correto que formata o preço

    def preco_promocional_formatado(self, obj):
        return obj.get_preco_promocional_formatado()  # Substitua pelo método correto que formata o preço promocional

    preco_formatado.short_description = 'Preço Formatado'
    preco_promocional_formatado.short_description = 'Preço Promocional Formatado'

    inlines = [VariacaoInline]


class VariacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'preco')  # Adicione outros campos que deseja exibir na lista
    fields = ['produto', 'preco']  # Campos a serem exibidos no formulário de edição
    # Adicione outros campos conforme necessário
    def get_preco(self, obj):
        return obj.preco  # Substitua por um método ou atributo que retorne o preço

    get_preco.short_description = 'Preço'  # Substitua pelo nome do campo 'preco' no modelo Variacao
    

admin.site.register(models.Produto, ProdutoAdmin) # Registrando a classe ProdutoAdmin para o modelo Produto
admin.site.register(models.Variacao, VariacaoAdmin) # Registrando o modelo Variacao