from django.shortcuts import render
from .import views
from .models import Post

def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'posts': data})
