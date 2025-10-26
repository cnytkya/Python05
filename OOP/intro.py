"""OOP'nin temel 4 ayağını gösterebiliriz.
1.Sınıf(class) ve Nesne(Object)
2.Kapsülleme(Enccapsulation)
3.Kalıtım(Inheritance)
4.Polimorfizm(Polymoprhism)
"""

# Sınıf(class) ve Nesne(Object): Py'da sınıf, bir taslaktır. Nesne ise bu taslaktan üretilmiş gerçek bir varlıktır.

#ör: sınıf tanımı
# def Ogrenci() metot
# class Ogrenci class

class Ogrenci:
    #bir nesne başlatılırken(init) önce özellikler atanır.
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_getir(self):
        print(f"Ad: {self.ad}, Yaş: {self.yas}")

#nesne oluşurma
ogrenci1 = Ogrenci("Cesur", 22)
ogrenci2 = Ogrenci("Selma", 25)
#sınırsız nesne oluşturulabilir.
ogrenci1.bilgileri_getir()
ogrenci2.bilgileri_getir()

#Burada Ogrenci sınıfı bir taslaktır(şablon), ogrenci1 ve ogrenci2 ise o taslaktan oluşturulmuş nesnelerdir.

# Kapsülleme(Enccapsulation): Verileri dışarıya kapatıp, sadece belirli fonksiyonlarla erişim sağlamaktır.

class BankaHesabi:
    def __init__(self,sahip,bakiye = 0):
        self.sahip = sahip
        self.__bakiye = bakiye # gizli(private) özellik
    
    def para_yatir(self,miktar):
        self.__bakiye += miktar #kullanıcı 10 tl eklerse yeni bakiye güncellenir.
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.__bakiye}")

    def para_cek(self,miktar):
        if miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.__bakiye}")
        else:
            print("Yetersiz bakiye!")

hesap = BankaHesabi("Ulvi", 100)
hesap.para_yatir(50)
hesap.para_cek(27)
# hesap.__bakiye

#Kalıtım(Inheritance): Bir sınıf, başka bir sınıfın özelliklerini miras alabilir.
class Hayvan:
    def __init__(self,isim):
        self.isim = isim
    
    def ses_cikar(self):
        print(f"{self.isim} bir ses çıkardı...")

class Kedi(Hayvan):
    def ses_cikar(self):
        print(f"{self.isim}: Miyav!")

class Kopek(Hayvan):
    def ses_cikar(self):
        print(f"{self.isim}: Hav Hav!")


#iki tane nesne oluşturduk
kedi = Kedi("Tekir")
kopek = Kopek("Karabaş")
x = Hayvan("Karga")

#nesnenin özelliklerini ekrana yazdıralım.

kedi.ses_cikar()
kopek.ses_cikar()
x.ses_cikar()

# Kedi



