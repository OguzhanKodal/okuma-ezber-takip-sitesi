from django.db import models

class okumatakip(models.Model):
    talebeno = models.CharField(max_length=15)
    ad = models.CharField(max_length=15)
    soyad = models.CharField(max_length=15)
    okumasayfa = models.IntegerField(null=True, blank=True) 
    kayittarihi = models.DateField(null=True)
    aktiflik = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad} - Talebe No: {self.talebeno} - Okuma Sayfa: {self.okumasayfa}- Kayıt Tarihi: {self.kayittarihi}"

class okumadetay(models.Model):
    kitapAdi = models.CharField(max_length=20)
    kitapAldigiTarih = models.DateField(null=True)
    toplamsayfa = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.kitapAdi
