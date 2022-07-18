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


class AdPostUpdateForm(forms.ModelForm):
    class Meta:
        model = models.AdPost
        fields = ('title', 'status', 'price', 'category', 'description')
        widgets = {
            'description': TinyMCE(),
        }
