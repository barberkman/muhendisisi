from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class SetPasswordForm(forms.Form):
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)

