from django.contrib import admin
from website.models.client import Client
from website.models.fact import Fact
from website.models.service import Service

admin.site.register(Client)
admin.site.register(Fact)
admin.site.register(Service)
