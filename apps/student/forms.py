from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'student_class', 'address', 'phone_number', 'login', 'password1', 'password2', 'photo', 'parents_number', 'parents_name','tariff', 'balance']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'student_class', 'address', 'phone_number', 'photo', 'parents_number', 'parents_name', 'tariff','balance']



class UserLoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')
        if login and password:
            user = authenticate(login=login, password=password)
            if user is None:
                raise forms.ValidationError("Invalid login or password.")
        return self.cleaned_data

class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['name', 'price']