from django import forms
from django.core.exceptions import ValidationError

from netflix.models import Movies, Categories

not_allowed_name = ["abc", "test", "dummy", "root"]


class CustomLoginForm(forms.Form):
    name = forms.CharField(max_length=233)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(CustomLoginForm, self).clean()
        name = self.cleaned_data.get("name")
        if name in not_allowed_name:
            ValidationError("name is not allowed")
