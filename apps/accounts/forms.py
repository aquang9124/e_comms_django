from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
class UserCreateForm(UserCreationForm):
	password1 = forms.CharField(label=("Password"),
		strip=False,
		widget=forms.PasswordInput(attrs={"class": "form-control"}),
	)
	password2 = forms.CharField(label=("Password Confirmation"),
		strip=False,
		widget=forms.PasswordInput(attrs={"class": "form-control"}),
	)
	class Meta:
		model = User
		
		widgets = {
			'username': forms.TextInput(attrs={"class": "form-control"}),
			'first_name': forms.TextInput(attrs={"class": "form-control"}),
			'last_name': forms.TextInput(attrs={"class": "form-control"}),
			'email': forms.EmailInput(attrs={"class": "form-control"}),
		}
		exclude = ['is_superuser', 'groups', 'user_permissions', 'date_joined', 'last_login', 'is_staff', 'is_active', 'password']

class AuthForm(AuthenticationForm):
	username = forms.CharField(
		max_length=254,
		widget=forms.TextInput(attrs={"class": "form-control"}),
	)

	password = forms.CharField(
		label = ("Password"),
		strip=False,
		widget=forms.PasswordInput(attrs={"class": "form-control"}),
	)