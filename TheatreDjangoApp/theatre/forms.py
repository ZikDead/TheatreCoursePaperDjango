from django import forms
from django.contrib.auth import authenticate, login


class LogInForm(forms.Form):
    username = forms.CharField (widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


    # def __init__(self):
    #       self._user = user

    def clean(self):
        if not authenticate(**self.cleaned_data):

            raise forms.ValidationError("Неверный логин\пароль")

    def auth(self):
        user = authenticate(**self.cleaned_data)
        if user is not None:
            return  user

# class MyForm(forms.ModelForm):
#     model = Post
#     fields = ['tittle', 'content'....]