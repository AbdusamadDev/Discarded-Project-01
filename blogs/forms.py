from django import forms

from blogs.models import BlogsModel


class BlogsCreationForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ["title", "content", "image"]


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ["title", "content", "image"]
