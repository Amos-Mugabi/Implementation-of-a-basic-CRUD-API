
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.UserListCreate.as_view(), name = 'users-list' ),
   
]
