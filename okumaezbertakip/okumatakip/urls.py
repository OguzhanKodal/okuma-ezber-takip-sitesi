from django.urls import path
from . import views

urlpatterns = [
    path('', views.okuma_listesi),
    path('oyenitalebe/', views.yenitalebe),  
    path('detay/<int:talebeno>/', views.talebedetay), 
    path('duzenle/<int:talebeno>/', views.talebeduzenle),

]