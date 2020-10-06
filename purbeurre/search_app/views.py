from re import sub as re_sub

from django.shortcuts import render
from django.views import View
from products_app.models import Product

from .configuration import STOP_WORDS


class ResultsView(View):

    def post(self, request, *args, **kwargs):
        input_user = request.POST['input_user']

        result = {'input_user': input_user}
        products = self._search_input_user(input_user)

        result.update({'products': products})
        return render(request, 'search_app/results.html',
                      {'result': result})

    def _search_input_user(self, input_user):
        """Search for products in database based on user input.

        Args:
            input_user (str): User input

        Return:
            products (list): List of products matching user input

        """

        parsed_input = self._parse_input_user(input_user)
        products = Product.objects.filter(
            name__unaccent__icontains=parsed_input).order_by('-nutriscore')
        # If user search match with products
        if products.count():
            return products

        return False

    def _parse_input_user(self, input_user):
        """Parse input user.

        Remove stop words and special characters.

        Args:
            input_user (str): Raw user input

        Return:
            parsed_input_user (str): Input user parsed

        """

        input_without_spec_chars = self._remove_special_characters(input_user)
        parsed_input = self._remove_stop_words(input_without_spec_chars)

        return parsed_input

    def _remove_special_characters(self, input):
        """Remove special characters.

        Args:
            input (str): Raw input

        Return:
            string (str): Input without special characters

        """

        re_spec_char = r'\W'

        return re_sub(re_spec_char, " ", input)

    def _remove_stop_words(self, input):
        """Remove stop words.

        Args:
            input (str): Sentence that might contains stop words.

        Return:
            words (list): List of words without stop words

        """

        return " ".join(
            [word.lower() for word in input.split() if word not in STOP_WORDS])
