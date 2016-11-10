from django import forms


class HomeContactForm(forms.Form):

    ur_email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Seu e-mail'}))
    ur_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    ur_message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensagem'}))