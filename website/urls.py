from django.urls import path
from .views.index import index
from .views.resume import resume

urlpatterns = [
    path("", index, name="index"),
    path(r'resume', resume, name="resume"),
]
