from django.urls import path
from . import views

urlpatterns = [
    path('', views.okuma_listesi),
    path('oyenitalebe/', views.yenitalebe),  
    path('odetay/<int:talebeno>/', views.talebedetay), 
    path('duzenle/<int:talebeno>/', views.talebeduzenle),
    path('ekle/<int:talebeno>/', views.okumaekle),

]