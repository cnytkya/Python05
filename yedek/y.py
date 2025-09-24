# main.py
# Bu dosya, uygulamanın ana menüsünü ve kullanıcı etkileşimini yönetir.

# os ve time kütüphanelerini içe aktarıyoruz.
# os: Ekranı temizlemek için işletim sistemi komutlarını çalıştırmak için kullanılır.
# time: Ekran temizlendikten sonra kısa bir bekleme eklemek için kullanılır.
import os
import time

# urunler.py modülünden gerekli fonksiyonları içe aktarıyoruz.
# Bu sayede bu fonksiyonları direkt olarak isimleriyle çağırabiliriz.
from x import urun_ekle, urunleri_listele, urun_sil

def ekran_temizle():
    """
    İşletim sistemine göre terminal ekranını temizler.
    Windows için 'cls', Linux/macOS için 'clear' komutunu kullanır.
    """
    # os.name 'nt' ise Windows demektir.
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1) # Kullanıcıya temizleme işlemini göstermek için 1 saniye bekler.

def menu_goster():
    """
    Kullanıcıya sunulan ana menüyü ekrana yazdırır.
    """
    print("\n--- Ürün Yönetim Uygulaması ---")
    print("1. Ürün Ekle")
    print("2. Ürünleri Listele")
    print("3. Ürün Sil")
    print("4. Ekranı Temizle")
    print("5. Çıkış")
    print("-------------------------------")

def uygulama():
    """
    Uygulamanın ana döngüsünü çalıştırır ve kullanıcı girdilerini yönetir.
    """
    while True: # Sonsuz döngü, kullanıcı çıkış yapana kadar çalışır.
        menu_goster()
        secim = input("Lütfen bir seçenek girin (1-5): ")

        if secim == '1':
            ad = input("Ürün adı: ")
            try:
                fiyat = float(input("Ürün fiyatı: ")) # Fiyatı float'a dönüştürmeyi dener.
                stok = int(input("Ürün stok adedi: ")) # Stok adedini integer'a dönüştürmeyi dener.
                urun_ekle(ad, fiyat, stok) # urunler modülündeki fonksiyonu çağırır.
            except ValueError:
                # Eğer girişler sayıya dönüştürülemezse hata mesajı verir.
                print("Hata: Fiyat ve stok sayı olmalıdır.")
        
        elif secim == '2':
            urunleri_listele() # urunler modülündeki fonksiyonu çağırır.
            
        elif secim == '3':
            try:
                urun_id = int(input("Silmek istediğiniz ürünün ID'sini girin: "))
                urun_sil(urun_id) # urunler modülündeki fonksiyonu çağırır.
            except ValueError:
                print("Hata: Ürün ID'si sayı olmalıdır.")
                
        elif secim == '4':
            ekran_temizle() # Ekran temizleme fonksiyonunu çağırır.

        elif secim == '5':
            print("Uygulamadan çıkılıyor...")
            break # Döngüden çıkarak uygulamayı sonlandırır.
            
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")

# Bu koşul, dosyanın doğrudan çalıştırıldığında içindeki kodun çalışmasını sağlar.
# Başka bir modül tarafından içe aktarıldığında bu kısım çalışmaz.
if __name__ == "__main__":
    uygulama()