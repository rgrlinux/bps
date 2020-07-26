from django.shortcuts import render
from .forms import ContactForm


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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem vindo ao formulário de contato",
        "form": contact_form,
    }
    return render(request, 'contact.html', context)
