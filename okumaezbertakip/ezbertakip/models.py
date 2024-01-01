from django.db import models

# Create your models here.

class ezbertakip(models.Model):
    talebeno = models.IntegerField(default=0)
    ad = models.CharField(max_length=15)
    soyad = models.CharField(max_length=15)
    ezber = models.CharField(max_length=25)
    kayittarihi = models.DateField(null=True)
    aktiflik = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}  {self.ezber} - Talebe No: {self.talebeno} -  Kayıt Tarihi: {self.kayittarihi}"

class ezberdetay(models.Model):
    ezberAdi = models.CharField(max_length=20)
    ezbereBasladiğiTarih = models.DateField(null=True)
    toplamezber = models.CharField(max_length=255)  

    def __str__(self):
        return self.ezberAdi

