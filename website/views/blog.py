from django.shortcuts import render
from website.models.blog import Blog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})
