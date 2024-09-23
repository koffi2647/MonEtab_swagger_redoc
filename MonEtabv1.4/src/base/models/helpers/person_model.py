import string

from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
#from scr.user.models.user_model import UserModel
from django.template.defaultfilters import slugify, random
from django.utils.crypto import get_random_string


# Create your models here.

class PersonModel(DateTimeModel):
    GENDER_CHOICES = (
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER'),
     )
    
    user = models.OneToOneField('user.CustomUserModel', on_delete=models.CASCADE)
    adress = models.OneToOneField('base.AdressModel', on_delete=models.CASCADE)
    birthday = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    url_picture = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    slug = models.SlugField(default="", blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            #self.slug = slugify(f'{self.last_name} {self.first_name}')
            self.slug = get_random_string(32)

        super(PersonModel, self).save(*args, **kwargs)












    # def slug_generator(self):
    #     return ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=20))
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = self.slug_generator()
    #         super(PersonModel, self).save()
    #     super(PersonModel, self).save()