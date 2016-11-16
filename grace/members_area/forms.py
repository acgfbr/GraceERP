from django import forms
from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField, BRCNPJField

from grace.members_area.models import Registration


class LoginForm(forms.Form):
    username = forms.CharField(label_suffix='', label='Usuário', max_length=51, required=True)
    password = forms.CharField(label_suffix='', label='Senha', max_length=36, widget=forms.PasswordInput, required=True)


class RegisterForm(forms.ModelForm):

    cnpj = BRCNPJField(label='CNPJ', required=False)
    cpf = BRCPFField(label='CPF', required=False)
    password = forms.CharField(label='Senha', max_length=36, widget=forms.PasswordInput, required=True)

    class Meta:
        model = Registration
        fields = ['username', 'password', 'name', 'cnpj', 'cpf', 'phone', 'email']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('phone') and not self.cleaned_data.get('email'):
            raise ValidationError('Informe seu telefone ou e-mail.')
        if not self.cleaned_data.get('cpf') and not self.cleaned_data.get('cnpj'):
            raise ValidationError('Informe seu cpf ou cnpj.')
        return self.cleaned_data