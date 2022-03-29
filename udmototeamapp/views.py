from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')