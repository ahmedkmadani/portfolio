from django.db import models


class About(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.CharField(max_length=500)
    title = models.CharField(max_length=250)


    def __str__(self) -> str:
        return self.name



class Service(models.Model):
    service_name = models.CharField(max_length=30)
    service_description = models.CharField(max_length=500)
    service_icon = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.service_name




class Testimonial(models.Model):
    testimonial_text = models.CharField(max_length=500)
    testimonial_picture = models.ImageField(upload_to='website/static/testimonial_img')
    testimonial_author = models.CharField(max_length=255)
    testimonial_firm = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.testimonial_text



class Fact(models.Model):
    happy_clinet = models.CharField(max_length=30)
    working_hours = models.CharField(max_length=30)
    awards_won = models.CharField(max_length=30)
    coffee_consumed = models.CharField(max_length=30)



class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_img = models.ImageField(upload_to='website/static/clients_img')

    def __str__(self) -> str:
        return self.client_name
