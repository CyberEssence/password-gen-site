from django import forms
import secrets

# input from for pass gen

class InputForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(min_value=8, max_value=64, required=True)
    use_uppercase = forms.BooleanField(required=False, initial=True)
    use_numbers = forms.BooleanField(required=False, initial=True)
