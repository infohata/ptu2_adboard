from django.shortcuts import render
from django.views import generic
from . import models


def index(request):
    return render(request, 'adboard_site/index.html')


class AdPostList(generic.ListView):
    model = models.AdPost
    template_name = 'adboard_site/adpost_list.html'
