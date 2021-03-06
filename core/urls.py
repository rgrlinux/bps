from django.urls import path
import core.views as v

urlpatterns = [
    path('', v.home_page, name='home'),
    path('about/', v.about_page, name='about'),
    path('contact/', v.contact_page, name='contact'),
    path('login/', v.login_page, name='login'),
    path('logout/', v.logout_page, name='logout'),
    path('register/', v.register_page, name='register'),
]