from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.AdPostList.as_view(), name='adpost_list'),
    
]
