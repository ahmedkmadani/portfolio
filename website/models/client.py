from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_img = models.ImageField(upload_to='website/static/clients_img')

    def __str__(self) -> str:
        return self.client_name
