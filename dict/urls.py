from django.urls import path, include
from .views import *

urlpatterns = [
    path('',homePage,name=''),
    path('search/',searchPage,name='search'),
]
