from django.contrib import admin
from website.models.client import Client
from website.models.fact import Fact
from website.models.service import Service
from website.models.about import About
from website.models.testimonial import Testimonial
from website.models.resume import Education, Experience, Certificates, SoftSkill, CodingSkill
from website.models.portfolio import Portfolio, Category



admin.site.register(Client)
admin.site.register(Fact)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(Testimonial)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificates)
admin.site.register(SoftSkill)
admin.site.register(CodingSkill)
admin.site.register(Portfolio)
admin.site.register(Category)


