from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class SchoolModel(NamedDateTimeModel):

    appSetting = models.OneToOneField('user.AppSettingModel', on_delete=models.CASCADE, related_name="user_app_setting_ids")
    url_logo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return f"{self.name}"