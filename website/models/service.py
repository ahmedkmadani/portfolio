from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=30)
    service_description = models.CharField(max_length=500)
    service_icon = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.service_name
