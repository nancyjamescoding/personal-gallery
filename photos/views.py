from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'photos/gallery.html')

def view_photo(request):
    return render(request, 'photos/photos.html')

def add_photo(request):
    return render(request, 'photos/add.html')
