from django.test import TestCase
from django.shortcuts import reverse
from pytest import mark
from search_app.views import ResultsView
from django.utils.encoding import smart_str

class TestPostSearch(TestCase):

    def test_post_return_status_code_and_correct_template(self):
        url = reverse('search_app:results')
        response = self.client.post(url, {'input_user': 'coca'})

        assert response.status_code == 200
        assert 'search_app/results.html' in [template.name for template in response.templates]

    def test_post_return_error_message_for_empty_result(self):
        url = reverse('search_app:results')
        response = self.client.post(url, {'input_user': 'gloubiboulga'})

        assert "Votre recherche n'a retourné aucun résultats" in smart_str(response.content)

input_and_expect_return = [
    ('Compote de pommes.',
     'compote pommes',
     ),
    ('Pot de nutella',
     'pot nutella',
     ),
    ('Confiture aux pruneaux',
     'confiture pruneaux',
     ),
    ('Sauce au pesto',
     'sauce pesto',
     ),
]

@mark.parametrize("input, expected", input_and_expect_return)
def test_parse_method_remove_stop_word_and_special_char(input, expected):
    search_result = ResultsView()
    assert search_result._parse_input_user(input) == expected

