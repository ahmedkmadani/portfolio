from django.db import models


class Testimonial(models.Model):
    testimonial_text = models.CharField(max_length=500)
    testimonial_picture = models.ImageField(upload_to='website/static/testimonial_img')
    testimonial_author = models.CharField(max_length=255)
    testimonial_firm = models.CharField(max_length=255)
