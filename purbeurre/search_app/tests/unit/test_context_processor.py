from django.test import TestCase
from search_app.context_processors import search_form
from search_app.forms import SearchForm


class ContextProcessorTest(TestCase):
    """Test search_app template context processor displaying a search form in
    base.html.
    """
    def setUp(self):
        """Setting up a context object. Passing an object as request."""
        requestObject = None
        self.context = search_form(requestObject)

    def test_search_form_return_a_dict(self):
        self.assertIsInstance(self.context, dict)

    def test_search_form_return_contain_correct_keys(self):
        for key_context, key_expect in zip(self.context.keys(),
                                           ['search_form']):
            self.assertEqual(key_context, key_expect)

    def test_search_form_return_contain_correct_values(self):
        for an_object, a_class in zip(self.context.values(), (SearchForm,)):
            self.assertIsInstance(an_object, a_class)
