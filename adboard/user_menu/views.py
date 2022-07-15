from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from . import forms


class UserCreate(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('sign_up_welcome')
    template_name = 'registration/user_create_form.html'


class UserCreateDone(generic.TemplateView):
    template_name = 'registration/user_create_done.html'


class UserUpdate(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.UserUpdateForm
    success_url = reverse_lazy('user_update')
    template_name = 'registration/user_update_form.html'
    queryset = get_user_model().objects.all()

    def get_object(self, queryset=get_user_model().objects.all()):
        return queryset.get(pk=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, _("User data has been updated successfully"))
        return super().form_valid(form)

