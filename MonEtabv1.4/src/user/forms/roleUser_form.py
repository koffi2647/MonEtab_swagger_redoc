from django import forms
from user.models.roleUser_model import RoleUserModel


class RoleUserForm(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = "__all__"
        