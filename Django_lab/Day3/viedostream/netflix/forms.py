from django import forms

from netflix.models import Movies, Categories


class CustomForm(forms.Form):
    name = forms.CharField(max_length=233)
    content = forms.CharField(widget=forms.Textarea)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:

        model = Categories
        fields = "__all__"
