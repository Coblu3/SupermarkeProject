from urunler import *
import time
s=market_veritabani()
print("""
***********************
Satıcı arayüzüne hoşgeldiniz...

Yeni ürün eklemek için 1'e basınız
Ürün silmek için 2'ye basınız
Tüm ürünleri görmek için 3'e basınız
Ürün verilerini güncellemek(eklemek,azaltmak) için 4'e basınız

çıkış için '0' a basınız...
************************
""")
while 1:
    secim=input("Seciminiz:")

    if int(secim)==0:
        print("Değişiklikler Yapılıyor Ve Çıkılıyor...")
        time.sleep(1)
        break

    elif  int(secim)==1:
        isim=input("Ürün İsmi:")
        fiyat=input("Ürün Fiyatı:")
        adet=input("Kaç Adet Ürün Ekleyeceksiniz:")

        s.yeni_urun_ekleme(isim,fiyat,adet)

    elif int(secim)==2:
        isim=input("Sileceğiniz Ürünün İsmi:")
        s.urun_sil(isim)

    elif int(secim)==3:
        s.urunleri_goster()

    elif int(secim)==4:
        isim=input("Güncellemek istediğiniz ürünün ismi:")
        s.urun_guncellemek(isim)


    else:
        break