from django.urls import path

from website.views import index, resume, portfolio, blog, contact

urlpatterns = [
    path("", index.index, name="index"),
    path(r'resume', resume.resume, name="resume"),
    path(r'portfolio', portfolio.portfolio, name="portfolio"),
    path(r'blog', blog.blog, name="blog"),
    path(r'contact', contact.contact, name="contact"),
]
