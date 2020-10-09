from django.shortcuts import reverse
from django.test import TestCase
from django.utils.encoding import smart_str


class TestPostSearch(TestCase):

    def test_post_return_status_code_and_correct_template(self):
        url = reverse('search_app:results')
        response = self.client.post(url, {'input_user': 'coca'})

        assert response.status_code == 200
        assert 'search_app/results.html' in [template.name for template in
                                             response.templates]

    def test_post_return_error_message_for_empty_result(self):
        url = reverse('search_app:results')
        response = self.client.post(url, {'input_user': 'gloubiboulga'})

        assert "Votre recherche n'a retourné aucun résultats" in smart_str(
            response.content)
