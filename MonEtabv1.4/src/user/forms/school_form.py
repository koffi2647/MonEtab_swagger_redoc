from django import forms
from user.models.school_model import SchoolModel


class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolModel
        fields = "__all__"
        