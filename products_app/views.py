from django.db.models import Count
from django.shortcuts import render

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
            'product_to_sub': product_to_sub
        })
        products_substitute = Product.objects.filter(
            categories__in=product_to_sub.categories.all(),
            nutriscore__lt=product_to_sub.nutriscore
        ).annotate(cat_common=Count('categories')
                   ).order_by('-cat_common', 'nutriscore')

        if products_substitute.count():
            result.update({'products': products_substitute[:10]})
        else:
            result.update({'products': False})

        return render(request, 'products_app/substitute.html',
                      {'result': result})


def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = False

    return render(request, 'products_app/product.html', {'product': product})
