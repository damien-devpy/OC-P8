from django.shortcuts import render
from django.views import View

from products_app.models import Product


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

        products = Product.objects.filter(
            name__icontains=input_user).order_by('-nutriscore')
        # If user search match with products
        if products.count():
            return products

        return False
