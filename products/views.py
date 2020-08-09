from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'list.html'

    def get_queryset(self):
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = 'featured-detail.html'
    queryset = Product.objects.all().featured()


# Class Based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'list.html'


# Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'list.html', context)


# Class based view
class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Esse produto não existe')
        return instance


# Function based view
def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Esse produto não existe')

    context = {
        'object': instance
    }
    return render(request, 'detail.html', context)
