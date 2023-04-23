from django.db import models


class CategoryBlog(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=5000)
    blog_date = models.DateField()
    blog_category  = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE)
    blog_img = models.ImageField(upload_to='blog/')


    def __str__(self) -> str:
        return self.title
