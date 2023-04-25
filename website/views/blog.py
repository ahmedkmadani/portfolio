from django.shortcuts import render
from website.models.blog import Blog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detailes(request, pk):
    blog = Blog.objects.filter(pk=pk).first()
    return render(request, 'blog-details.html', {'blog': blog})
