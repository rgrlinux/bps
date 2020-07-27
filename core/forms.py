from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class ContactForm(forms.Form):
    full_name = forms.CharField(
        error_messages={'required': 'Coloque seu nome cabra!'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Full name',
             }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid': 'Email inválido seu cabra'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Já existe este usuário.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Já existe este email')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('As senhas informadas não estão iguais!')
        return data
