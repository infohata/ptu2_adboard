from django import forms
from tinymce.widgets import TinyMCE
from . import models


class AdPostForm(forms.ModelForm):
    class Meta:
        model = models.AdPost
        fields = ('title', 'price', 'category', 'description')
        widgets = {
            'description': TinyMCE(),
        }


class AdPostUpdateForm(AdPostForm):
    class Meta:
        fields = ('title', 'status', 'price', 'categpry', 'description')

