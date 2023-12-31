from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import okumatakip
from django.views.decorators.csrf import csrf_exempt

def okuma_listesi(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        okumatakip.objects.get(id = silinecek).delete()
    okumalistesi = okumatakip.objects.all().values()
    okumasablon = loader.get_template('okumalist.html')
    okumaVeri = {
        'okumalistesi' : okumalistesi
    }
    return HttpResponse(okumasablon.render(okumaVeri,request))



@csrf_exempt
def yenitalebe(request):
    bilgi = {'yeniKayit': "False"}

    if request.method == 'POST':
        ad = request.POST.get('adi', '')
        soyad = request.POST.get('soyadi', '')
        talebeno = request.POST.get('talebeno', '')
        kayittarihi = request.POST.get('kayittarihi', '')
        okumasayfa = request.POST.get('okumasayfa','')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            aktiflik = True

        yeniTalebe = okumatakip(ad=ad, soyad=soyad, talebeno=talebeno,
                                kayittarihi=kayittarihi, okumasayfa=okumasayfa,
                                aktiflik=aktiflik)
        yeniTalebe.save()
        bilgi = {'yenitalebe': "True"}

    ytsablon = loader.get_template('oyeniekle.html')
    return HttpResponse(ytsablon.render(bilgi, request))


def talebedetay(request, talebeno):
    detay = {'talebe': okumatakip.objects.get(id=talebeno)}
    dsablon = loader.get_template('detay.html')
    return HttpResponse(dsablon.render(detay, request))


def talebeduzenle(request, talebeno):

    talebe = okumatakip.objects.get(id=talebeno)

    guncellendimi = "False"

    if request.method == 'POST':

        talebe.ad = request.POST.get('adi', '')
        talebe.soyad = request.POST.get('soyadi', '')
        talebe.talebeno = request.POST.get('talebeno', '')
        talebe.kayittarihi = request.POST.get('kayittarihi', '')
        talebe.okumasayfa = request.POST.get('okumasayfa','')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            talebe.aktiflik = True
        else:
            talebe.aktiflik = False

        talebe.save()

        guncellendimi = "True"

    duzenle = {'talebe': talebe, 'guncellendimi': guncellendimi}

    sablon = loader.get_template('duzenle.html')
    return HttpResponse(sablon.render(duzenle, request))