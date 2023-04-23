from django.shortcuts import render
from website.models.about import About, Service, Testimonial, Client, Fact



def index(request):
    clinets = Client.objects.all()
    for i in clinets:
          print(i.client_img)
    facts = Fact.objects.first()
    services = Service.objects.all()
    about = About.objects.first()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'clinets': clinets,
                                          'facts': facts, 'services': services,
                                            'about': about, 'testimonials': testimonials})
