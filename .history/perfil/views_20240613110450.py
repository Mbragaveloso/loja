from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import copy

from . import models
from . import forms


class BasePerfil(View):
    template_name = 'perfil/criar.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho', {}))

        self.perfil = None
    
        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user
            ).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None,
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
            ),
            'perfilform': forms.PerfilForm(
                data=self.request.POST or None
            )
        }

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']
    
        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
    def POST(self, *args, **kwargs):
       #if not self.userform.is_valid() or not self.perfilform.is_valid():
        if not self.userform.is_valid():
            return self.renderizar
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('passeord')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        idade = self.userform.cleaned_data.get('idade')
        data_nascimento = self.userform.cleaned_data.get('data_nascimento')
        endereco = self.userform.cleaned_data.get('endereco')
        numero = self.userform.cleaned_data.get('numero')
        cep = self.userform.cleaned_data.get('cep')
        cidade = self.userform.cleaned_data.get('cidade')
        estado = self.userform.cleaned_data.get('estado')
        
        
        # usuario logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)
            
            usuario.username = username
            
            if password:
                usuario.set_password(password)
                
            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()
                
        # usuario nao log
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()
            
            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            
        if password:
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password
                )

            if autentica:
                login(self.request, user=usuario)
           
        self.request.session['carrinho'] = self.carrinho
        self.request.session.save()
        return self.renderizar
    
class Atualizar(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'perfil/atualizar.html')
    
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