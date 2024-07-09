from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class BaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("As senhas não coincidem")

        if password and len(password) < 6:
            raise forms.ValidationError("A senha deve ter pelo menos 6 caracteres")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserForm(BaseForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Senha',
        help_text='Digite pelo menos 6 caracteres'
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'email')
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'E-mail',
        }
        help_texts = {
            'username': 'O nome de usuário deve conter no máximo 150 caracteres. Apenas letras, números e @/./+/-/_ são permitidos.',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

class PerfilForm(BaseForm):
    class Meta:
        model = Perfil
        fields = []  # Aqui você pode listar os campos do modelo Perfil que deseja incluir no formulário
        labels = {
            # Labels personalizados para os campos do modelo, se necessário
        }