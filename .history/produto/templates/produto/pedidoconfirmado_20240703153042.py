{% extends 'base.html' %}
{% load omfilters %}
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'custom/css/style.css' %}">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

<main class="container mt-4 mb-4">
    <div class="row mt-3">
        <div class="col">
            <h1>Pedido confirmado com Sucesso</h1>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Produto</th>
                        <th scope="col">Preço Unitário</th>
                        <th scope="col">Quantidade</th>
                        <th scope="col">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    {% for produto in produtos %}
                    <tr>
                        <td class="align-middle">
                            {% if linha.imagem %}
                            <img class="cart-img" src="{{ linha.imagem }}" alt="{{ linha.produto_nome }}" style="width: 50px; height: auto;">
                            {% else %}
                                <img class="cart-img" src="{% static 'path/to/default-image.jpg' %}" alt="Imagem padrão" style="width: 50px; height: auto;">
                            {% endif %}
                        </td>
                    <tr>
                        <td class="d-none d-lg-bloc"></td>
                        <td>{{ produto.produto_nome }}</td>
                        <td>R$ {{ produto.preco_unitario|floatformat:2 }}</td>
                        <td>{{ produto.quantidade }}</td>
                        <td>R$ {{ produto.subtotal|floatformat:2 }}</td>
                    </tr>
                    {% endfor %}
                    <tr>
                        <td colspan="3" class="text-right">Total:</td>
                        <td>R$ {{ total|floatformat:2 }}</td>
                    </tr>
                </tbody>
            </table>
            
            <form method="post" action="{% url 'produto:pedidoconfirmado' %}">
                {% csrf_token %}
                <button type="submit" class="btn btn-primary">Finalizar Compra</button>
            </form>
        </div>
    </div>
</main>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function() {
        $('.remover-item').click(function() {
            var variacaoId = $(this).data('variacao-id');
            $.ajax({
                url: '/remover/' + variacaoId + '/',
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    window.location.reload();
                }
            });
        });
    });
</script>

{% endblock %}