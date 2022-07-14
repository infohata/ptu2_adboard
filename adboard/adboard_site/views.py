from django.shortcuts import render


def index(request):
    return render(request, 'adboard_site/index.html')
