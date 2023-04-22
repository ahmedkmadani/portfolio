from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Portfolio(models.Model):
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    project_date = models.CharField(max_length=255)
    project_descripiton = models.CharField(max_length=255)
    project_link = models.CharField(max_length=255)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='website/static/project_img', null=True)

    def __str__(self) -> str:
        return self.project_name




