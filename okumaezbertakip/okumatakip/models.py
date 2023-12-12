from django.db import models

class okumatakip(models.Model):
    num = models.CharField(max_length=15)
    ad = models.CharField(max_length=15)
    soyad = models.CharField(max_length=15)
    okumasayfa = models.IntegerField(default=0)  
    kayitTarihi = models.DateField(null=True)
    aktiflik = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class okumadetay(models.Model):
    kitapAdi = models.CharField(max_length=20)
    kitapAldigiTarih = models.DateField(null=True)
    toplamsayfa = models.IntegerField()

    def __str__(self):
        return self.kitapAdi
