from django.contrib import admin
from .models import okumatakip
from .models import okumadetay

# Register your models here.

class okumatakipAdmin(admin.ModelAdmin):
    list_display = ("talebeno", "ad", "soyad", "kayittarihi","aktiflik",)
    empty_value_display = "BOŞ"

class okumadetayAdmin(admin.ModelAdmin):
    list_display = ("okumaKitap", "okumayaBasladigiTarih", "okumaSayfa")
    empty_value_display = "BOŞ"

admin.site.register(okumatakip, okumatakipAdmin)
admin.site.register(okumadetay,okumadetayAdmin)

