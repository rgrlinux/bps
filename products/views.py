from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


# Class Based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


# Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'list.html', context)


# Class based view
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


# Function based view
def product_detail_view(request, pk=None, *args, **kwargs):
    #    instance = get_object_or_404(Product, pk=pk)
    try:
        instance = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        print('Nenhum produto encontrado aqui!')
        raise Http404('Esse produto não existe')
    except:
        print('uhuuu')

    context = {
        'object': instance
    }
    return render(request, 'detail.html', context)
