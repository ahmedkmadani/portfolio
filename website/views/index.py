from django.shortcuts import render
from website.models.client import Client
from website.models.fact import Fact
from website.models.service import Service

def index(request):
    clinets = Client.objects.all()
    facts = Fact.objects.first()
    services = Service.objects.all()
    return render(request, 'index.html', {'clinets': clinets,
                                          'facts': facts, 'services': services})
