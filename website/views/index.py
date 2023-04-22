from django.shortcuts import render
from website.models.client import Client
from website.models.fact import Fact
from website.models.service import Service
from website.models.about import About
from website.models.testimonial import Testimonial



def index(request):
    clinets = Client.objects.all()
    facts = Fact.objects.first()
    services = Service.objects.all()
    about = About.objects.first()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'clinets': clinets,
                                          'facts': facts, 'services': services,
                                            'about': about, 'testimonials': testimonials})
