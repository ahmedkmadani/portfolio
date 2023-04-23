from django.db import models


class Education(models.Model):
    university_name = models.CharField(max_length=255)
    university_year = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    major_description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.university_name



class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    job_description = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.company_name



class Certificates(models.Model):
    certi_logo = models.ImageField(upload_to='cert/')
    certi_title = models.CharField(max_length=255)
    certi_id = models.CharField(max_length=255)
    certi_date = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.certi_title



class SoftSkill(models.Model):
    skill = models.CharField(max_length=255)
    skill_precntage = models.IntegerField()

    def __str__(self) -> str:
        return self.skill


class CodingSkill(models.Model):
    skill = models.CharField(max_length=255)
    skill_precntage = models.IntegerField()

    def __str__(self) -> str:
        return self.skill
