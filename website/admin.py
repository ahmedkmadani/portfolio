from django.contrib import admin
from website.models.client import Client
from website.models.fact import Fact
from website.models.service import Service
from website.models.about import About


admin.site.register(Client)
admin.site.register(Fact)
admin.site.register(Service)
admin.site.register(About)

