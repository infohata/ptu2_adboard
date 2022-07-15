from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, forms as user_forms
from django.utils.translation import gettext_lazy as _


class UserCreateForm(user_forms.UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ("username", "email", )
        field_classes = {"username": user_forms.UsernameField}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name", )
        field_classes = {"username": user_forms.UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user_with_email = get_user_model().objects.filter(email=email).exclude(username=username)
        if not user_with_email.exists():
            return email
        else:
            raise ValidationError(_('User with this email address already exists'))
