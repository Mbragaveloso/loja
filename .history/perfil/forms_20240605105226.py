from django import forms
from . import models


class PerfilForms(forms.ModelForm):
    class Meta:
        models = models


class UserForm(forms.ModelForm):
    pass



