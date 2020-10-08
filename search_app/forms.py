from django import forms


class SearchForm(forms.Form):
    """Create a search form. Allow the user searching for a product."""
    input_user = forms.CharField(label="Cherchez un aliment de substitution",
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Recherchez un produit'
                                 }))
