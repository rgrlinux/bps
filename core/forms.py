from django import forms


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
