rom django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def login(request):
    return render(request, 'login.html')
