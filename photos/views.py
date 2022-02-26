from django.shortcuts import render
from django.template import context
from .models import Category, Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos=Photo.objects.all()
    context = {'categories':categories, 'photos': photos}
    return render(request,'photos/gallery.html', context)

def view_photo(request, pk):
    photos=Photo.objects.get(id=pk)
    return render(request,'photos/photos.html', {'photo': photos})

def add_photo(request):
    return render(request,'photos/add.html')          