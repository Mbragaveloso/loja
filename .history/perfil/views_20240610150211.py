from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy


from . import models
from . import forms

class BasePerfil(View):
    template_name = 'perfil/criar.html'
    
    def get_context_data(self, **kwargs):
        return {
            'user_form': forms.UserForm(data=self.request.POST or None),
            'perfil_form': forms.PerfilForm(data=self.request.POST or None)
        }
    
    def get(self, request, *args, **kwargs):
        contexto = self.get_context_data()
        return render(request, self.template_name, contexto)
    
    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(request.POST)
        perfil_form = forms.PerfilForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            # Faça algo com os dados dos formulários (salvar no banco de dados, por exemplo)
            # ...
            return HttpResponse('Dados salvos com sucesso!')  # ou redirecione para outra página
        else:
            contexto = self.get_context_data()
            return render(request, self.template_name, contexto)



class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('perfil:criar')

        usuario = authenticate(
            self.request, username=username, password=password)

        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('perfil:criar')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Você fez login no sistema e pode concluir sua compra.'
        )
        return redirect('produto:carrinho')


class Logout(View):
    def get(self, *args, **kwargs):
        carrinho = copy.deepcopy(self.request.session.get('carrinho'))

        logout(self.request)

        self.request.session['carrinho'] = carrinho
        self.request.session.save()

        return redirect('produto:lista')