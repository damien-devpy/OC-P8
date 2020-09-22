from django import forms

class SearchForm(forms.Form):
    input_user = forms.CharField(label="Cherchez un aliment de substitution", max_length=100)