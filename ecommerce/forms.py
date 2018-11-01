from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()