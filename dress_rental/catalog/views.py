from django.shortcuts import render, get_object_or_404
from .models import Dress

def home(request):
    dresses = Dress.objects.all()
    return render(request, 'catalog/home.html', {'dresses':dresses})

def catalog(request):
    dresses = Dress.objects.all()
    return render(request, 'catalog/catalog.html', {'dresses':dresses})

def catalog_detail(request, dress_id):
    dress = get_object_or_404(Dress, pk = dress_id)
    return render(request, 'catalog/dress_detail.html', {'dress': dress})

def contact(request):
    return render(request, 'catalog/contact.html')

def conditions(request):
    return render(request, 'catalog/conditions.html')