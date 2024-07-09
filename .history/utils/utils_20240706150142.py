def formata_preco(val):
    try:
        # Converte o valor para um número de ponto flutuante
        val = float(val)
        # Formata o preço
        return f'R${val:.2f}'.replace('.', ',')
    except (ValueError, TypeError):
        return val  # Retorna o valor original se não puder ser convertido para float

def cart_total_qtd(user):
    try:
        carrinho = Carrinho.objects.get(usuario=user)
        return carrinho.itens.count()
    except Carrinho.DoesNotExist:
        return 0

def cart_totals(carrinho):
    return sum(
        float(item.get('preco_unitario_promocional') or item.get('preco_unitario') or 0) * int(item.get('quantidade', 0))
        for item in carrinho.values()
    )