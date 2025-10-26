# Temel sınıf
class Kisi:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
    
    def bilgileri_goster(self):
        print(f"Ad: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}")

class Ogrenci(Kisi):
    def __init__(self, ad, soyad, yas,ogrenci_no):
        super().__init__(ad, soyad, yas)
        self.ogrenci_no = ogrenci_no
        self.__notlar = {}
    
    def not_ekle(self,ders,notu):
        self.__notlar[ders] = notu

    def notlari_goster(self):
        print(f"{self.ad} {self.soyad} - Notlar: ")
        for ders, notu in self.__notlar.items():
            print(f"{ders}: {notu}")

class Ogretmen(Kisi):
    def __init__(self, ad, soyad, yas,brans):
        super().__init__(ad, soyad, yas)
        self.brans = brans
    
    def bilgileri_goster(self):
        print(f"Öğretmen adı: {self.ad},Soyad: {self.soyad},Yaş: {self.yas}, Branş: {self.brans}")

class Ders():
    def __init__(self, ad, ogretmen):
        self.ad = ad
        self.ogretmen = ogretmen
        self.ogrenciler = []
    
    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
    
    def ders_bilgileri(self):
        print(f"Ders: {self.ad} - Öğretmen: {self.ogretmen.ad}, {self.ogretmen.soyad}")
        print("Kayıtlı Öğrenciler:")
        for ogr in self.ogrenciler:
            print(f"-{ogr.ad}, {ogr.soyad}")

#nesneleri oluştur
#Öğretmen oluştur
ogretmen1 = Ogretmen("Aslı", "Soylu",30,"Mat" )
#Öğrenci oluştur
ogrnci1 = Ogrenci("Mehmet", "Kaya",16, "7")
ogrnci2 = Ogrenci("Nazım", "Hikmet",16, "71")
#ders oluştur
mat_dersi = Ders("Mat",ogretmen1)

#öğrencileri derse ekle
mat_dersi.ogrenci_ekle(ogrnci1)
mat_dersi.ogrenci_ekle(ogrnci2)

#öğrencilere not ekle
ogrnci1.not_ekle("Mat", 98)
ogrnci2.not_ekle("Mat", 96)

#bilgileri göster
ogretmen1.bilgileri_goster()
mat_dersi.ders_bilgileri()
ogrnci1.notlari_goster()
ogrnci2.notlari_goster()


