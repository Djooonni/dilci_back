from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
    soz = forms.CharField(label='Sözün başlanğıc formasını daxil edin', max_length=100)
    round_list=['Isim','Feil', 'Sifet', 'Say','Zerf','Evezlik']
    nitq = forms.ChoiceField(choices=tuple([(name, name) for name in round_list]))

class TextForm(forms.Form):
    metn = forms.CharField(label='Mətni daxil edin', max_length=1000,widget=forms.Textarea)
    round_list=['Bizim Alqoritm']#,'Porter Alqoritmi','Lancaster Alqoritmi','WordNet Alqoritmi']
    alqo = forms.ChoiceField(choices=tuple([(name, name) for name in round_list]))

class SozForm(forms.Form):
    soz=forms.CharField(label='Sözü daxil edin', max_length=100)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )
