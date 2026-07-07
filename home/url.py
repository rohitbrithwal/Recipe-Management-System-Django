# ye new url.py bnate taki jo bhi print krana hai khi se bhi project ke 
#andr direct yhi likh sake

from . import views  # taki issi home file ke andr ko access kr sake
from django.urls import path

# Import only what we need (avoid wildcard + missing-name issues)
from vege.views import recipie, delete_recipie, update_recipie

urlpatterns = [
    path('', views.home, name='home'),
    path('sum/', views.sum, name='sum'),
    path('recipie/', recipie, name='recipie'),
    path('delete/<id>/', delete_recipie, name='delete_recipie'),
    path('update/<id>/', update_recipie, name='update_recipie'),
    path('html/', views.html, name='html'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

