from django.db import models

# Create your models here.
class Portfolio(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Açıqlama")
    age = models.CharField(max_length=100, verbose_name="Yaş")
    date_of_birth = models.CharField(max_length=100, verbose_name="Doğum Tarixi")
    location = models.CharField(max_length=100, verbose_name="Yer")
    education = models.CharField(max_length=100, verbose_name="Təhsil")
    skills = models.CharField(max_length=100, verbose_name="Bacarıqlar")
    experience = models.CharField(max_length=100, verbose_name="Təcrübə")
    project = models.CharField(max_length=100, verbose_name="Proyekt")
    contact = models.CharField(max_length=100, verbose_name="Əlaqə")