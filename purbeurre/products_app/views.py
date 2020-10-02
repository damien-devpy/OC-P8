from django.db.models import Count
from django.forms import model_to_dict
from django.shortcuts import render, reverse
from products_app.models import Product


def substitute(request, product_id):
    try:
        product_to_sub = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'products_app/substitute.html',
                      {'result': False})
    else:
        result = {
            'product_to_sub': model_to_dict(product_to_sub)
        }

        product_substitute = Product.objects.filter(
            categories__in=product_to_sub.categories.all()
            ).annotate(cat_common=Count('categories')
                       ).order_by('-cat_common', 'nutriscore')[0]

        if product_to_sub.id != product_substitute.id and product_to_sub.nutriscore > product_substitute.nutriscore:
            result.update({'product_substitute': model_to_dict(product_substitute)})

        return render(request, 'products_app/substitute.html', {'result': result})

