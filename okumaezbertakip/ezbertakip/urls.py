from django.urls import path
from . import views

urlpatterns = [
    path('', views.ezber_listesi),
    path('yenitalebe/', views.yenitalebe),  
    path('detay/<int:talebeno>/', views.talebedetay), 
    path('duzenle/<int:talebeno>/', views.talebeduzenle),
    path('ekle/<int:talebeno>/', views.ezberekle),

]
