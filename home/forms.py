from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].required = True

    class Meta:
        model = User
        fields = ['email', 'password']
