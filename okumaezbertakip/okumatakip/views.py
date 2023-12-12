from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import okumatakip
import datetime
from django.views.decorators.csrf import csrf_exempt


def okumatakip(request):
    okumasablon = loader.get_template('okumalist.html')
    return HttpResponse(okumasablon.render())

def talebeDetay(request, talebeno):
    return HttpResponse(str(talebeno) + " no'lu talebe detayı")

@csrf_exempt
def yenitalebe(request):
    bilgi = {'yeniKayit': "False"}

    if request.method == 'POST':
        adi = request.POST.get('adi', '')
        soyadi = request.POST.get('soyadi', '')
        talebeno = request.POST.get('talebeno', '')
        kayittarihi = request.POST.get('kayittarihi', '')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            aktiflik = True

        yeniTalebe = okumatakip(ad=adi, soyad=soyadi, talebeno=talebeno,
                                kayittarihi=kayittarihi,
                                aktiflik=aktiflik)
        yeniTalebe.save()
        bilgi = {'yenitalebe': "True"}

    ytsablon = loader.get_template('yeniekle.html')
    return HttpResponse(ytsablon.render(bilgi, request))