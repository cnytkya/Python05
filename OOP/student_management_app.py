# gerçek nesneler oluşturun. json dosyasına kayıtları kaydeden bir öğrenci yönetim sistemi oluşturun.
import json
import os

# sınıflar

class Kisi:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def to_dict(self):
        return {
            "ad":self.ad,
            "soyad":self.soyad,
            "yas":self.yas
        }
    
class Ogrenci(Kisi):
    def __init__(self, ad, soyad, yas,ogr_no):
        super().__init__(ad, soyad, yas)
        self.ogr_no = ogr_no
        self.notlar = {}
    
    def not_ekle(self,ders,notu):
        self.notlar[ders] = notu
    
    def to_dict(self):
        data = super().to_dict()
        data.update({ 
            "ogr_no":self.ogr_no,
            "notlar":self.notlar
        })
        return data
    
class Ogretmen(Kisi):
    def __init__(self, ad, soyad, yas,brans):
        super().__init__(ad, soyad, yas)
        self.brans = brans
    
    def to_dict(self):
        data = super().to_dict()
        data.update({ 
            "brans":self.brans
        })
        return data
    
class Ders:
    def __init__(self, ad, ogretmen):
        self.ad = ad
        self.ogretmen = ogretmen
        self.ogrenciler = []
        
    def ogrenci_ekle(self,ogrenci):
        self.ogrenciler.append(ogrenci)
    
    def to_dict(self):
        return {
            "ad":self.ad,
            "ogretmen":self.ogretmen.to_dict(),
            "ogrenciler": [ogr.to_dict() for ogr in self.ogrenciler]
        }
    
# JSON Kaydetme ve Yükleme
class VeriTabani:
    def __init__(self, dosya_adi = "veriler.json"):
        self.dosya_adi = dosya_adi
        self.veri = {"ogrenciler": [], "ogretmenler" : [], "dersler" : []}
        self.yukle()

    def kaydet(self):
        with open(self.dosya_adi, "w", encoding="utf-8") as f:
            json.dump(self.veri, f, ensure_ascii=False, indent=4)
    
    def yukle(self):
        if os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, "r", encoding= "utf-8") as f:
                self.veri = json.load(f)


db = VeriTabani()

#öğretmen ekle
ogrt1 = Ogretmen("Ahmet","Şafak",55, "Türkçe")
db.veri["ogretmenler"].append(ogrt1.to_dict())
    
#öğrenci ekle
ogr1 = Ogrenci("Kenan","Yılmaz",22, "10")
ogr2 = Ogrenci("Sezin","Kaya",18, "22")

ogr1.not_ekle("Mat", 95)
ogr2.not_ekle("Mat", 100)

db.veri["ogrenciler"].append(ogr1.to_dict())
db.veri["ogrenciler"].append(ogr2.to_dict())


#ders ekle
mat_dersi = Ders("Mat",ogrt1)
mat_dersi.ogrenci_ekle(ogr1)
mat_dersi.ogrenci_ekle(ogr2)

db.veri["dersler"].append(mat_dersi.to_dict())

db.kaydet()

print("Veriler 'veriler.json' dosyasına kaydedildi.")