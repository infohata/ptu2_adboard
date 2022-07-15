from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.UserCreate.as_view(), name='sign_up'),
    path('sign_up/welcome/', views.UserCreateDone.as_view(), name='sign_up_welcome'),
    path('update/', views.UserUpdate.as_view(), name='user_update'),
]
