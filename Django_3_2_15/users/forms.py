from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserChangeProfileBasic(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    password = None

    class Meta:
        model = User
        fields = [
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name
        ]


class UserChangeProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (Profile.birthday.field.name, Profile.image.field.name)
