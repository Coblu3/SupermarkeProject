import _sqlite3


class Urunler():
    def __init__(self, urun , fiyat , adet):
       self.urun=urun
       self.fiyat=fiyat
       self.adet=adet

    def __str__(self):
        return "\n{} = {}TL \nStok Durumu {} Adet ".format(self.urun,self.fiyat,self.adet)


class market_veritabani():
    def __init__(self):
        self.baglanti = _sqlite3.connect("Veritabani.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists urunlistesi(Urun TEXT,Fiyat INT,Adet INT)")
        self.baglanti.commit()

    def fiyat_degistirme(self, isim):
        komut = "update from urunlistesi where Urun=?"
        self.cursor.execute(komut, isim, )
        self.baglanti.commit()

    def yeni_urun_ekleme(self, isim, fiyat,adet):
        komut = "Insert Into urunlistesi Values(?,?,?)"
        self.cursor.execute(komut, (isim, fiyat, adet,))
        self.baglanti.commit()
    def urun_kontrol(self,isim):
        komut = "Select * From urunlistesi where isim=?"
        self.cursor.execute(komut,(isim,))
        urunler = self.cursor.fetchall()
        if len(urunler) != 0:
            print("Böyle bir ürün bulunmamakta")
            return 0




    def urunleri_goster(self):
        komut="Select * From urunlistesi"
        self.cursor.execute(komut)
        urunler=self.cursor.fetchall()
        if len(urunler)!=0:
            for i in urunler:
                urun=Urunler(i[0],i[1],i[2])
                print(urun)
                print("*********")
        else:
            print("Ürün bulunmamakta")
    def urun_satin_al(self,isim,secim):
        global adet,statik
        komut="Select * From urunlistesi Where Urun = ?"
        self.cursor.execute(komut,(isim,))
        urun=self.cursor.fetchall()
        for i in urun:
            adet=i[2]
            statik=adet

        adet-=secim
        if adet<0:
            print("Ne yazık ki elimizde {} ürün bulunmamakta elimizde yalnızca {} ürün var... ".format(secim,statik))
        else:
            komut2="Update urunlistesi Set Adet=? where Urun =?"
            self.cursor.execute(komut2,(adet,isim))
            self.baglanti.commit()

    def urun_sil(self,isim):
        komut="Delete From urunlistesi Where Urun=? "
        self.cursor.execute(komut,(isim,))
        self.baglanti.commit()
    def urun_guncellemek(self,isim):
        global adet
        komut="Select * from urunlistesi Where Urun=?"
        self.cursor.execute(komut,(isim,))
        urun=self.cursor.fetchall()
        secim=input("Ürün Eklemek istiyorsanız 'E' Çıkarmak istiyorsanız 'Ç'")
        if secim =='e':
            miktar=int(input("Kaç adet eklemek istiyorsunuz"))
            for i in urun:
                adet=i[2]
                adet+=miktar
        elif secim=='ç':
            miktar=int(input("Kaç adet çıkarmak istiyorsunuz"))
            for i in urun:
                adet=i[2]
                adet-=miktar
        komut2="Update urunlistesi Set Adet=? Where Urun = ?"
        self.cursor.execute(komut2,(adet,isim,))
        self.baglanti.commit()

