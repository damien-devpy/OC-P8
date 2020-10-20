from django.test import TestCase

from search_app.forms import SearchForm


class ContextProcessorTest(TestCase):
    """Test search_app template context processor displaying a search form in
    base.html.
    """

    def test_context_processor_return_expected_data(self):
        response = self.client.get('/')
        form_context = response.context.get('search_form')
        self.assertIsNotNone(form_context)
        self.assertIsInstance(form_context, SearchForm)

    def test_context_processor_return_expected_data2(self):
        response = self.client.get('/login/')
        form_context = response.context.get('search_form')
        self.assertIsNotNone(form_context)
        self.assertIsInstance(form_context, SearchForm)
