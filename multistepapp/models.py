from django.db import models


class Appl(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)


class AcademicInstitution(models.Model):
    institution = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    achivements = models.FileField(upload_to='media/%Y/%m/%d')
    appl = models.ForeignKey(Appl, on_delete=models.CASCADE, null=True)
