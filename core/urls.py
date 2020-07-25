from django.urls import path
import core.views as v

urlpatterns = [
    path('', v.home_page, name='index'),
    path('about/', v.about_page, name='about'),
    path('contact/', v.contact_page, name='contact'),
]
