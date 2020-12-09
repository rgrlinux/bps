from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import *


def home_page(request):
    context = {
        "title": "Bem vindos",
        "content": "Bem vindo"
    }
    if request.user.is_authenticated:
        context['premium_content'] = 'You are a premium user'
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


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print('User logged in')
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)

        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            print('Login válido')
            return redirect('/')
        else:
            print('Login inválido')
    return render(request, 'auth/login.html', context)


def logout_page(request):
    context = {
        'content': 'Você efetuou logout com sucesso!'
    }
    logout(request)
    return render(request, 'auth/logout.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)
