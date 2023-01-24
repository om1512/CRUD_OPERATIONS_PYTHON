from django import forms
from .models import BlogModel

# creating a form
class BlogForms(forms.ModelForm):
# create meta class
    class Meta:
    # specify model to be used
        model = BlogModel
        # specify fields to be used
        fields = [
        "title",
        "description",
        ]