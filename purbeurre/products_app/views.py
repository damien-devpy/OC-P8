from django.db.models import Count
from django.forms import model_to_dict
from django.shortcuts import render, reverse
from products_app.models import Product


def substitute(request, product_id):
    result = {}
    try:
        product_to_sub = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'products_app/substitute.html',
                      {'result': False})
    else:
        result.update({
            'product_to_sub': model_to_dict(product_to_sub)
        })

        products_substitute = Product.objects.filter(
            categories__in=product_to_sub.categories.all()
            ).annotate(cat_common=Count('categories')
                       ).order_by('-cat_common', 'nutriscore')

        result.update({'products': [model_to_dict(product_substitute) for product_substitute in products_substitute]})
        return render(request, 'products_app/substitute.html', {'result': result})

