from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comentario, Avaliacao, Perfil

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("As senhas não coincidem.")
        return data['password2']
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota']

class EditarPerfilForm(forms.ModelForm):
    telefone = forms.CharField(required=False, max_length=15, label="Telefone")
    cep = forms.CharField(required=False, max_length=9, label="CEP")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos do modelo User

    def save(self, commit=True):
        user = super().save(commit=False)  # Salva os dados do modelo User
        if commit:
            user.save()
            # Atualiza ou cria o perfil associado
            Perfil.objects.update_or_create(
                usuario=user,
                defaults={
                    'telefone': self.cleaned_data.get('telefone'),
                    'cep': self.cleaned_data.get('cep'),
                }
            )
        return user