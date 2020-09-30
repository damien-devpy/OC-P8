from django.shortcuts import render

def substitute(request, product_id):

    return render(request, 'products_app/substitute.html', {'product_id': product_id})
