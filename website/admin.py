from django.contrib import admin
from website.models.client import Client
from website.models.fact import Fact


admin.site.register(Client)
admin.site.register(Fact)
