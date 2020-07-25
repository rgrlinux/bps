from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Bem vindos",
        "content": "Bem vindo"
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        "title": "About page",
        "content": "About page"
    }
    return render(request, 'about.html', context)


def contact_page(request):
    context = {
        "title": "Contact",
        "content": "Contact"
    }
    return render(request, 'Contact.html', context)
