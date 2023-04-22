from django.db import models


class About(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.CharField(max_length=500)
    title = models.CharField(max_length=250)


    def __str__(self) -> str:
        return self.name
