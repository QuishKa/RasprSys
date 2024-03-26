from django import forms

class NameForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
