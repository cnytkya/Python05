# urunler.py
# Bu dosya, uygulamanın temel veri yönetimini (ürün ekleme, listeleme, silme) yapar.

import json  # JSON verilerini okuyup yazmak için Python'ın yerleşik kütüphanesi
import os    # Dosya sistemi işlemlerini (dizin oluşturma, dosya yolu birleştirme) yapmak için

# Veri dosyalarının saklanacağı dizin adını tanımlıyoruz.
# Uygulama çalıştığında bu isimde bir klasör oluşturulacak.
DOSYA_DIZINI = 'veriler'

# JSON dosyasının tam yolunu oluşturuyoruz.
# os.path.join() fonksiyonu, işletim sistemine (Windows, Linux, macOS)
# özel dosya yolu ayraçlarını otomatik olarak doğru şekilde ekler.
# Örnek: 'veriler/urun_kayitlari.json'
DOSYA_ADI = os.path.join(DOSYA_DIZINI, 'urun_kayitlari.json')

def json_oku():
    """
    JSON dosyasını okur ve içeriğini bir Python listesi olarak döndürür.
    Dosya yoksa veya boşsa, boş bir liste döndürerek hata oluşmasını engeller.
    """
    # os.path.exists() ile dosyanın varlığını, os.path.getsize() ile boş olup olmadığını kontrol ederiz.
    if os.path.exists(DOSYA_ADI) and os.path.getsize(DOSYA_ADI) > 0:
        # Dosyayı okuma ('r') modunda, Türkçe karakterler için 'utf-8' ile açarız.
        with open(DOSYA_ADI, 'r', encoding='utf-8') as f:
            # json.load() ile JSON verisini Python listesine dönüştürür.
            return json.load(f)
    else:
        # Dosya yoksa veya boşsa, boş bir liste döndürürüz.
        return []

def json_yaz(urunler):
    """
    Verilen Python listesini JSON formatında dosyaya yazar.
    """
    # İlk olarak veri dizininin varlığını kontrol ederiz.
    # Eğer dizin yoksa os.makedirs() ile oluştururuz.
    if not os.path.exists(DOSYA_DIZINI):
        os.makedirs(DOSYA_DIZINI)
    
    # Dosyayı yazma ('w') modunda, Türkçe karakterler için 'utf-8' ile açarız.
    with open(DOSYA_ADI, 'w', encoding='utf-8') as f:
        # json.dump() ile Python listesini JSON formatına dönüştürüp yazarız.
        # indent=4: Dosyanın daha okunabilir olması için girinti ekler.
        # ensure_ascii=False: Türkçe karakterlerin düzgün yazılmasını sağlar.
        json.dump(urunler, f, indent=4)

def urun_ekle(ad, fiyat, stok):
    """
    Yeni bir ürünü okuyup JSON dosyasına kaydeder.
    """
    urun_listesi = json_oku() # Mevcut ürün listesini dosyadan oku.
    
    # Yeni bir ID oluşturur.
    # Eğer liste boşsa ilk ID'yi (1) atar, değilse son ID'nin bir fazlasını kullanır.
    if not urun_listesi:
        yeni_id = 1
    else:
        yeni_id = max(urun['id'] for urun in urun_listesi) + 1
    
    # Yeni ürün için bir sözlük oluştururuz.
    yeni_urun = {
        'id': yeni_id,
        'ad': ad,
        'fiyat': fiyat,
        'stok': stok
    }
    
    urun_listesi.append(yeni_urun) # Yeni ürünü listeye ekleriz.
    json_yaz(urun_listesi)         # Güncellenmiş listeyi tekrar dosyaya yazarız.
    print(f"'{ad}' adlı ürün başarıyla eklendi. ID: {yeni_id}")

def urunleri_listele():
    """
    JSON dosyasındaki tüm ürünleri okuyup ekrana yazdırır.
    """
    urun_listesi = json_oku() # Dosyadan tüm ürünleri okur.
    
    if not urun_listesi:
        print("Listede hiç ürün bulunmuyor.")
        return
        
    print("\n--- Ürün Listesi ---")
    for urun in urun_listesi: # Her bir ürünü döngüyle ekrana yazdırırız.
        print(f"ID: {urun['id']} | Ad: {urun['ad']} | Fiyat: {urun['fiyat']} TL | Stok: {urun['stok']}")
    print("---------------------\n")

def urun_sil(urun_id):
    """
    Belirtilen ID'ye sahip ürünü dosyadan siler.
    """
    urun_listesi = json_oku() # Dosyadan ürün listesini okur.
    
    # List Comprehension kullanarak silinecek ürün dışındaki tüm ürünleri yeni bir listeye alırız.
    urun_listesi_yeni = [urun for urun in urun_listesi if urun['id'] != urun_id]
    
    # Eğer yeni liste ile eski listenin uzunluğu aynıysa, silinecek ürün bulunamamıştır.
    if len(urun_listesi_yeni) == len(urun_listesi):
        print(f"Hata: ID {urun_id} ile eşleşen bir ürün bulunamadı.")
    else:
        json_yaz(urun_listesi_yeni) # Güncellenmiş listeyi dosyaya yazarız.
        print(f"ID {urun_id} olan ürün başarıyla silindi.")