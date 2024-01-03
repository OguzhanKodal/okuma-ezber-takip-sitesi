from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import ezbertakip, ezberdetay
from django.views.decorators.csrf import csrf_exempt

def ezber_listesi(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        ezbertakip.objects.get(id = silinecek).delete()
    ezberlistesi = ezbertakip.objects.all().values()
    ezbersablon = loader.get_template('ezberlist.html')
    ezberVeri = {
        'ezberlistesi' : ezberlistesi
    }
    return HttpResponse(ezbersablon.render(ezberVeri,request))


@csrf_exempt
def yenitalebe(request):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    bilgi = {'yeniKayit': "False"}

    if request.method == 'POST':
        ad = request.POST.get('adi', '')
        soyad = request.POST.get('soyadi', '')
        talebeno = request.POST.get('talebeno', '')
        kayittarihi = request.POST.get('kayittarihi', '')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            aktiflik = True

        yeniTalebe = ezbertakip(ad=ad, soyad=soyad, talebeno=talebeno,
                                 kayittarihi=kayittarihi,
                                aktiflik=aktiflik)
        yeniTalebe.save()
        bilgi = {'yenitalebe': "True"}

    ytsablon = loader.get_template('yeniekle.html')
    return HttpResponse(ytsablon.render(bilgi, request))


def talebedetay(request, talebeno):
    kullanici = ezbertakip.objects.get(id=talebeno)
    ezberleri = ezberdetay.objects.filter(kullanici=kullanici)

    detay = {'talebe': kullanici,'ezberleri':ezberleri}

    dsablon = loader.get_template('detay.html')
    return HttpResponse(dsablon.render(detay, request))


def talebeduzenle(request, talebeno):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")

    talebe = ezbertakip.objects.get(id=talebeno)

    guncellendimi = "False"

    if request.method == 'POST':

        talebe.ad = request.POST.get('adi', '')
        talebe.soyad = request.POST.get('soyadi', '')
        talebe.talebeno = request.POST.get('talebeno', '')
        talebe.ezber = request.POST.get('ezber','')
        talebe.kayittarihi = request.POST.get('kayittarihi', '')

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

def ezberekle (request, talebeno):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")

    talebe = ezbertakip.objects.get(id=talebeno)
    guncellendimi = "False"
    if request.method == 'POST':

        ezberAdi = request.POST.get('ezberAdi', '')
        ezbereBasladigiTarih= request.POST.get('ezbereBasladigiTarih', '')
        ezberSayisi = request.POST.get('ezberSayisi', '')
        
        yeniEzber = ezberdetay(ezberAdi=ezberAdi, ezbereBasladigiTarih=ezbereBasladigiTarih,
                                 ezberSayisi=ezberSayisi,
                                kullanici=talebe)
        yeniEzber.save()

        guncellendimi = "True"

    ekle = {'talebe': talebe, 'guncellendimi': guncellendimi}

    sablon = loader.get_template('ezberekle.html')
    return HttpResponse(sablon.render(ekle, request))

