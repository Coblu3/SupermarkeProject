from urunler import *
import time

s = market_veritabani()
print("""
********************
Erdal Bakkala Hoşgeldiniz...
Ürünlerimizi Görmek için 1'e basınız
Satın almak için 2'ye basınız

çıkış için '0' a basınız

********************
""")
while 1:
    secim = input("Seciminiz:")

    if int(secim) == 1:
        s.urunleri_goster()

    elif int(secim) == 2:
        s.urunleri_goster()
        isim=input("Satın Alacağınız Ürünün İsmi:")
        adet=int(input("Kaç adet almak istiyorsunuz:"))
        s.urun_satin_al(isim,adet)

    elif int(secim)==0:
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        print("Yine bekleriz...")
        break


    else:
        break
