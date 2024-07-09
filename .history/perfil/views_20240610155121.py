from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy

''
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

class Criar(BasePerfil):
    def post(self, request, *args, **kwargs):
        contexto = self.get_context_data()
        user_form = contexto['user_form']
        perfil_form = contexto['perfil_form']
        
        
        if not user_form.is_valid() or not perfil_form.is_valid():
            messages.error(
                request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )
            return render(request, self.template_name, contexto)

        username = user_form.cleaned_data.get('username')
        password = user_form.cleaned_data.get('password')
        email = user_form.cleaned_data.get('email')
        first_name = user_form.cleaned_data.get('first_name')
        last_name = user_form.cleaned_data.get('last_name')
        
        # Usuário logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, username=self.request.user.username)

            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not perfil_form:
                perfil_form.cleaned_data['usuario'] = usuario
                print(perfil_form.cleaned_data)
                perfil = models.Perfil(**perfil_form.cleaned_data)
                perfil.save()
            else:
                perfil = perfil_form.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        # Usário não logado (novo)
        else:
            usuario = user_form.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = perfil_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password:
            autentica = authenticate(
                request,
                username=usuario.username,
                password=password
            )

            if autentica:
                login(request, user=usuario)

        request.session['carrinho'] = carrinho
        request.session.save()

        messages.success(
            request,
            'Seu cadastro foi criado ou atualizado com sucesso.'
        )

        messages.success(
            request,
            'Você fez login e pode concluir sua compra.'
        )

        return redirect('produto:carrinho')

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