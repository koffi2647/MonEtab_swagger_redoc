from django import forms
from user.models.appSetting_model import AppSettingModel


class AppSettingForm(forms.ModelForm):
    class Meta:
        model = AppSettingModel
        fields = "__all__"
        