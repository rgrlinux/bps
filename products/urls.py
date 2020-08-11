from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>', ProductDetailSlugView.as_view()),
]
