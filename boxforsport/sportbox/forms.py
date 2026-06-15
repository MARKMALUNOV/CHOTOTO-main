from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть логін'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'})
    )