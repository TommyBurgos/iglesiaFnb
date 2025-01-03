from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('sobreNosotros', views.aboutUs),
]