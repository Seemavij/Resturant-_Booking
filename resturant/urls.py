from django.urls import path
from . import views

app_name = 'resturant'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='resturant'),
      
]