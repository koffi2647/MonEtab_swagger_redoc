from django import forms
from user.models.custom_user_model import CustomUserModel


class UserFoms(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = [
            'username',
            'password',
            'roleUser',
            'school',
        ]
        