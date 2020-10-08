from django.shortcuts import reverse
from django.test import TestCase
from django.utils.encoding import smart_str


class TestFavoritesView(TestCase):

    def setUp(self):
        url = reverse('favorites_app:favorites')
        self.response = self.client.get(url)

    def test_get_return_expected_page(self):
        assert 'favorites_app/favorites.html' in [template.name for template in
                                                  self.response.templates]
        assert 200 == self.response.status_code

    def test_get_favorites_without_authentication_return_error(self):
        assert "Vous n'êtes pas connecté." in smart_str(self.response.content)
        assert "nutriscore" not in smart_str(self.response.content)
