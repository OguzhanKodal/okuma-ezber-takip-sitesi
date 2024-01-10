from django.db import models

class okumatakip(models.Model):
    talebeno = models.CharField(max_length=15)
    ad = models.CharField(max_length=15)
    soyad = models.CharField(max_length=15)
    kayittarihi = models.DateField(null=True)
    aktiflik = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad} - Talebe No: {self.talebeno} - Kayıt Tarihi: {self.kayittarihi}"

class okumadetay(models.Model):
    okumaKitap = models.CharField(max_length=20)
    okumayaBasladigiTarih = models.DateField(null=True)
    okumaSayfa = models.IntegerField(null=True)
    kullanici = models.ForeignKey(okumatakip, on_delete = models.CASCADE,
                                  related_name = 'kullanici', null=True)
    def __str__(self):
          return f"{self.okumaKitap} {self.okumaSayfa}"
