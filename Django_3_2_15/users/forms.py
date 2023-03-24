from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserChangeProfile(forms.Form):
    email = forms.EmailField(label='Электронная почта', required=False)
    name = forms.CharField(max_length=255, label='Имя', required=False)
    surname = forms.CharField(max_length=255, label='Фамилия', required=False)
    birthday = forms.DateField(
        label='Дата рождения',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
        )
    userpic = forms.ImageField(label='Аватарка', required=False)
