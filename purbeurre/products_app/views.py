from django.shortcuts import render
from django.forms import model_to_dict
from django.db.models import Count
from products_app.models import Product, Category

def substitute(request, product_id):
    try:
        product_to_sub = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'products_app/substitute.html', {'result': False})
    else:
        product_substitute = Product.objects.filter(categories__in=product_to_sub.categories.all()
                                                    ).annotate(cat_common=Count('categories')
                                                               ).order_by('-cat_common','nutriscore')
        result = {
            'product_to_sub': model_to_dict(product_to_sub),
            'product_substitute': model_to_dict(product_substitute[0]),
        }
        return render(request, 'products_app/substitute.html', {'result': result})


