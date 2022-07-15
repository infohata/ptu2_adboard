from django import forms
from django.contrib.auth import get_user_model, forms as user_forms


class UserCreateForm(user_forms.UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ("username", "email", )
        field_classes = {"username": user_forms.UsernameField}
