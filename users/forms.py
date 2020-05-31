from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class': 'email-imput form-control',
        'style': 'margin-top:10px;',
        'placeholder': 'Username',
        'minlength': '6',
        'required': '',
    }))
    
    password = forms.CharField(widget = forms.PasswordInput (
        attrs = {
            'class': 'password-input form-control',
            'style': 'margin-top:10px',
            'required': '',
            'placeholder': 'Password',
            'minlength': '6',
            
        }))