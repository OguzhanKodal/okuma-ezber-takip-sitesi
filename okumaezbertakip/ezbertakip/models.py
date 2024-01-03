from django.db import models

# Create your models here.

class ezbertakip(models.Model):
    talebeno = models.IntegerField(default=0)
    ad = models.CharField(max_length=15)
    soyad = models.CharField(max_length=15)
    kayittarihi = models.DateField(null=True)
    aktiflik = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad} - Talebe No: {self.talebeno} -  Kayıt Tarihi: {self.kayittarihi}"

class ezberdetay(models.Model):
    ezberAdi = models.CharField(max_length=20)
    ezbereBasladigiTarih = models.DateField(null=True)
    ezberSayisi = models.IntegerField(null=True)  
    kullanici = models.ForeignKey(ezbertakip, on_delete = models.CASCADE,
                                  related_name = 'kullanici', null=True)
    

    def __str__(self):
        return self.ezberAdi

