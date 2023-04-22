from django.db import models


class Fact(models.Model):
    happy_clinet = models.CharField(max_length=30)
    working_hours = models.CharField(max_length=30)
    awards_won = models.CharField(max_length=30)
    coffee_consumed = models.CharField(max_length=30)
