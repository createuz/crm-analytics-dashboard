from django.shortcuts import render

from django.shortcuts import render


def dashboard(request):
    return render(request, 'index.html')


def product_list(request):
    return render(request, 'product-list.html')
