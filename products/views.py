from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


# Class Based view
class ProductListView(ListView):
    queryset = Product.objects.all()


# Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs':queryset
    }
    return render(request, 'products/list.html', context)
