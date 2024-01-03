from django.contrib import admin
from .models import ezbertakip
from .models import ezberdetay

# Register your models here.

class ezbertakipAdmin(admin.ModelAdmin):
    list_display = ("talebeno", "ad", "soyad","kayittarihi","aktiflik",)
    empty_value_display = "BOŞ"

class ezberdetayAdmin(admin.ModelAdmin):
    list_display = ("ezberAdi", "ezbereBasladigiTarih", "ezberSayisi")
    empty_value_display = "BOŞ"

admin.site.register(ezbertakip, ezbertakipAdmin)
admin.site.register(ezberdetay,ezberdetayAdmin)
