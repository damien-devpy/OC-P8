from django.shortcuts import render
from django.views import View

class Favorites(View):
    """View managing favorites user.

    GET method display all favorites is the user is authenticated.
    POST method allow to register a product to favorites user.

    """

    def get(self, request):
        result = {}
        if request.user.is_authenticated:
            result.update(
                {'products': request.user.favorites.all()}
            )

        return render(request, 'favorites_app/favorites.html', {'result': result})

    def post(self, request):
        result = {}
        if request.user.is_authenticated:
            product_substitute = request.POST['product_substitute']
            request.user.favorites.add(product_substitute)
            result.update({'products': request.user.favorites.all()},
                          )

        return render(request, 'favorites_app/favorites.html', {'result': result})


