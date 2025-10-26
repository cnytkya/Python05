#Bu dosya, uygulamanın ana menüsü ve kullanıcı etkileşimini yönetir.

import os
import time

from urunler import urun_ekle,urunleri_listele,urun_sil

def ekran_temizle():
    """
    İşletim sistemine göre terminal ekranını temizler.
    """
    time.sleep(2) # Ekran temizliği iin 2 sn bekletir.
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """
    Kullanıcıya sunulan ana menüyü ekrana yazdırır.
    """
    print("\n======Ürün Yönetim Uygulaması=======")
    print("1.Ürün Ekle")
    print("2.Ürün Listele")
    print("3.Ürün Sil")
    print("4.Ekranı Temizle")
    print("5.Çıkış")

def uygulama():
    """
    Uygulamanın ana döngüsünü çalıştırır ve kullanıcı girdilerini yönetir.
    """
    while True:
        menu()
        secim = int(input("Lütfen bir seçenek girin(1-5): "))
        
        if secim == 1:
            ad = input("Ürün Adı: ")
            try:
                fiyat = float(input("Ürün Fiyatı: "))
                stok = int(input("Ürün Adedi: "))
                urun_ekle(ad,fiyat,stok)
            except ValueError:
                #Eğer girişler sayıya dönüştürülmezse hata mesajı verir.
                print("Hata: Fiyat ve stok sayı tipinde olmalı!!!")
        elif secim == 2:
            urunleri_listele()
        elif secim == 3:
            try:
                urun_id = int(input("Silmek istediğiniz ürün ID: "))
                urun_sil(urun_id)
            except ValueError:
                print("Ürün ID'si tam sayı olmalıdır.")
        elif secim == 4:
            ekran_temizle()
        elif secim == 5:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. 1-5 arasında seçim yapınız!")    
            
if __name__ == "__main__":
    uygulama()