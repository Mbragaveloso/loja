from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import copy

from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False, 
        widget=forms.PasswordInput(),
        label='Senha',
        help_text='Digite pelo menos 6 caracteres'
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',
                  'password2', 'email')
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("As senhas não coincidem")

        if password and len(password) < 6:
            raise forms.ValidationError("A senha deve ter pelo menos 6 caracteres")

        usuario_data = cleaned_data.get('username')
        email_data = cleaned_data.get('email')
        password_data = cleaned_data.get('password')
        password2_data = cleaned_data.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_password_match = 'As duas senhas não conferem'
        error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracteres'
        error_msg_required_field = 'Este campo é obrigatório.'

        validation_error_msgs = {}

        # Usuários logados: atualização
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

        # Usuários não logados: cadastro
        else:
            if usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists
                
            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field
                
            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field
                
            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise forms.ValidationError(validation_error_msgs)

        return cleaned_data
    
class CriarPerfilView(View):
    template_name = 'perfil/criar.html'
    
    def get(self, request):
        # Instanciar os formulários vazios
        user_form = UserForm()
        perfil_form = PerfilForm()
        
        # Passar os formulários para o template
        context = {'user_form': user_form, 'perfil_form': perfil_form}
        
        # Renderizar o template com os formulários
        return render(request, self.template_name, context)
    
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