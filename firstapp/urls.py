from django.urls import path
from requests import request
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:section>', views.category, name='category'),
    path('view/<int:id>', views.view, name='view'),
    path('search/', views.search, name='search'),
    path('', views.email, name="email"),
]
