from django.shortcuts import render
from website.models.client import Client
from website.models.fact import Fact

def index(request):
    clinets = Client.objects.all()
    facts = Fact.objects.first()
    return render(request, 'index.html', {'clinets': clinets, 'facts': facts})
