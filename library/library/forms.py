from django import forms

class EmailForm(forms.Form):
    your_email = forms.CharField(label='Email', max_length=100)