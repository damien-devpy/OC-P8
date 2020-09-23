from django import forms


class SearchForm(forms.Form):
    input_user = forms.CharField(label="Cherchez un aliment de substitution",
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Recherchez un produit'
                                 }))
