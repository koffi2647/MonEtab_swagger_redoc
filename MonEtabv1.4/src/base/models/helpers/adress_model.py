from django.db import models


# Create your models here.
class AdressModel(models.Model):

    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Adress"
        verbose_name_plural = "Adress"

    def __str__(self):
        return f"{self.street}, {self.city}"