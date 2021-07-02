from django import forms

from main.models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['created_at']
