from unicodedata import category
from django.shortcuts import render, redirect
from django.template import context
from .models import Category, Photo

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)  

    categories = Category.objects.all()
    context = {'categories':categories, 'photos': photos}
    return render(request,'photos/gallery.html', context)

def view_photo(request, pk):
    photos=Photo.objects.get(id=pk)
    return render(request,'photos/photos.html', {'photo': photos})

def add_photo(request):
    return render(request,'photos/add.html')          