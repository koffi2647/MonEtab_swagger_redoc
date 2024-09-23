from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserModel(AbstractUser):
    roleUser = models.ManyToManyField('user.RoleUserModel', default=1)
    school = models.ForeignKey('user.SchoolModel', on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}, {self.school}"