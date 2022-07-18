from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.AdPostList.as_view(), name='adpost_list'),
    path('<int:pk>/', views.AdPostDetail.as_view(), name='adpost_detail'),
    path('<int:pk>/reserve/', views.adpost_reserve, name='adpost_reserve'),
    path('<int:pk>/sell/', views.adpost_sell, name='adpost_sell'),
    path('<int:pk>/reject/', views.adpost_reject, name='adpost_reject'),
]
