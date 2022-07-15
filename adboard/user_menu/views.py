from django.contrib.auth import get_user_model
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms


class UserCreate(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('sign_up_welcome')
    template_name = 'registration/user_create_form.html'


class UserCreateDone(generic.TemplateView):
    template_name = 'registration/user_create_done.html'
