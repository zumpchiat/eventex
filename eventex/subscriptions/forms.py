from django import forms

class SubForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='Cpf')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
