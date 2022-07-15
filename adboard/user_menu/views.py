from django.contrib.auth import get_user_model, forms as user_forms
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy


class UserCreate(generic.CreateView):
    form_class = user_forms.UserCreationForm
    success_url = reverse_lazy('sign_up_welcome')
    template_name = 'registration/user_create_form.html'


class UserCreateDone(generic.TemplateView):
    template_name = 'registration/user_create_done.html'
