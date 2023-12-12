from django.urls import path
from . import views

urlpatterns = [
    path('', views.okumatakip),
    path('yenitalebe', views.yenitalebe),
    path('<int:talebeno>', views.talebeDetay)
]
