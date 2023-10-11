from . import views
from django.urls import path ,include

urlpatterns = [
# URL of Api

#url of html pages
path('', views.index,name="index"),
path('refresh_data/', views.refresh_data,name="refresh_data"),


]