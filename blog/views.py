from django.shortcuts import render

from .models import Blog
# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/all_blogs.html', {'blogs' : blogs})