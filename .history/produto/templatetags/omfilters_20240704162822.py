from django import template
from utils import utils


register = template.Library()

@register.filter
def formata_preco(val):
    return utils.formata_preco(val)

@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)

@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)

@register.filter(name='cart_total_qtd')
def cart_total_qtd(value):
    # Lógica do filtro
    return value

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
    
@register.filter
def custom_sum(value, arg):
    try:
        return float(value) * float(arg)
    except(ValueError, TypeError):
        return 0 
