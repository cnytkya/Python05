# Ürün Yönetim Uygulaması
import os # os Python'nın işletim sistemiyle çalışmasını sağlayan dahili kütüphanesi. harici kütüphaneleri kullanabilmek için pip install libname ör->pip install pandas,numpy

# Windows için : os.system("cls")
# Linux / Mac için : os.system("clear")

#ekranı temizlyen bir metot yazalım.
def temizle():
    os.system("cls" if os.name == "nt" else "clear") # Burası py'daki ternary tek satırlık if-else yapısıdır. Eğer os.name == "nt" ise "cls" kullan değilse "clear" kullan. os.name işletim sistemini söyler. 
# Not: nt aslında Windows NT ailesine verilen isimden gelir. W'un çekirdeği(kernel) windows NT üzerine kuruludur. O yüzden py, işletim sistemini kontrol ederken windows için "nt" döndürür.

#Not: os,sys,math,datetime gibi kütüphaneler py'ın içinde hazır gelir. harici kütüphaneleri kullanabilmek için pip install libname ör->pip install pandas,numpy


# Ürünleri tutmak için boş bir liste oluşturalım. CRUD->Create,Read,Update,Delete
urunler = [] # urunler global bir değişkendir.

while True:
    print("-------------Ürün Yönetim uygulaması-----------")
    print("1 - Ürün Ekle")
    print("2 - Ürünleri Listele")
    print("3 - Ürün Sil")
    print("4 - Ürün Ara")
    print("0 - Çıkış")

    choice = int(input("Seçiminizi yapınız: ")) # choice yerel bir değişkendir.

    if choice == 1:
        urun = input("Eklenecek ürün ismi: ")
        #urunler listesine kullanıcıdan aldığımız değeri atıyoruz.
        urunler.append(urun)
        print(f"{urun} ürünü eklendi")
    elif choice == 2:
        if len(urunler) == 0:#eğer listede eleman yoksa(eleman yoksa uzunluğu 0 olur.)
            print("Listede ürün bulunamadı!")
        else:
            print("Ürün Listesi:")
            for i, u in enumerate(urunler,1):
                print(f"{i}. {u}")
    elif choice == 3:
        silinecek = input("Silmek istediğiniz ürün adı: ")
        if silinecek in urunler:
            urunler.remove(silinecek)
            print(f"{silinecek} ürünü silindi")
        else:
            print("Ürün bulunamadı!")
    elif choice == 4:
        aranacak_urun = input("Aramak istediğiniz ürün adını yazınız: ")
        if aranacak_urun in urunler:
            print(f"{aranacak_urun} bulundu.")
        else:
            print("Ürün bulunamadı!")
    elif choice == 0:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Tekrar deneyiniz.")
    #Kullanıcı entere'a basarsa temizle fonksiyonu çalışsın, yoksa bekle.
    girdi = input("\nDevam etmek için Enter tuşuna basınız: ")
    if girdi == "":
        temizle()
 