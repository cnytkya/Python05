# Bu modül, ürün verilerini JSON dosyasına kaydedecek ve bu dosyadan okuyacak.

# metotlar: veri yönetimi için ürün ekleme,silme,listeleme...
import os
import json
# oluşacak dosyanın dizini
DOSYA_DIZINI = 'veriler'
DOSYA_ADI = os.path.join(DOSYA_DIZINI, 'urunler.json') 
#JSON dosyasının tam yolunu oluşturduk. os.path.join() fonksiyonu, işletim sistemine göre (windows,linux,macOS)
# özel dosya yolu araçlarını otomatik olarak doğru şekilde ekler.
# Örnek: "veriler/urunler.json"

def json_oku():
    """
    JSON dosyasını okur ve içeriğini bir py listesi olarak döndürür.
    Dosya yokse veya boşsa, boş bir liste döndürerek hata alınmasını engeller.
    """

    if os.path.exists(DOSYA_ADI) and os.path.getsize(DOSYA_ADI) > 0:
        #Dosyayı okuma("r") modunda, Türkçe karakterler için 'utf-8' ile açarız.
        with open(DOSYA_ADI, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return [] # dosya yoksa veya boş ise boş bir liste döndürür.

def json_yaz(urunler):
    """
    Verilen py listesini JSON formatında dosyaya yazar.
    """
    #ilk olarak veri dizinin varlığını kontrol ederiz. Eğer dizin yoksa os.makedirs(DOSYA_DIZINI) ile oluştururuz.
    if not os.path.exists(DOSYA_DIZINI):
        os.makedirs(DOSYA_DIZINI)
    
    # Dosyayı yazma ('w') modunda, türkçe karakterler için utf-8 charset'ni kullanırız
    with open(DOSYA_ADI, 'w', encoding= "utf-8") as f:
        json.dump(urunler,f, indent=4)

def urun_ekle(ad,fiyat,stok):
    """
    Yeni bir ürünü okuyup JSON dosyasına kayder.
    """
    urun_listesi = json_oku() # Mevcut ürün listesini dosyadan oku.

    # Yeni bir ID oluştur. Eğer liste boşsa ilk ID'yi (1) atar, değilse son ID'nin bir fazlasını kullanır
    if not urun_listesi:
        yeni_id = 1
    else:
        yeni_id = max(urun['id'] for urun in urun_listesi()) + 1
    
    #Yeni ürün için bir sözlük oluşturalım
    yeni_urun = {
        'id' : yeni_id,
        'ad' : ad,
        'fiyat' : fiyat,
        'stok' : stok,
    }

    urun_listesi.append(yeni_urun) #yeni ürünü burda listeye ekliyoruz.
    json_yaz(urun_listesi) # Güncellenmiş listeyi tekrar dosyaya yazarız.
    print(f"{ad} adlı ürün başarıyla eklendi. ID: {yeni_id}")

def urunleri_listele():
    """
    JSON dosyasındaki tüm ürünleri okuyacak ve ekranda göstercek
    """
    urun_listesi = json_oku()
    #eğer listede ürün yoksa
    if not urun_listesi:
        print("Listede hiç ürün bulunmuyor.")
        return
    print("\n===============Ürünler Listesi=========================")
    for urun in urun_listesi:#her ürünü döngüyle ekrana yazdırır
        print(f"ID: {urun['id']} | Ürün Adı: {urun['ad']} | Ürün Fiyatı: {urun['fiyat']} | Ürün Adedi: {urun['stok']} ")
        print("**********************************************\n")

def urun_sil(urun_id):
    """
    Belirtilen id'ye göre ürün silinecek
    """
    urun_listesi = json_oku()# Dosyadan ürün listesini okur.
    # List Comprehension kullanarak silinecek ürün dışındaki tüm ürenleri yeni bir listeye atacak.
    urun_listesi_yeni = [urun for urun in urun_listesi if urun['id' != urun_id]]

    #Eğer yeni liste ile eski listenin uzunluğu aynıysa, silinecek ürün bulunamadı yazsın
    if len(urun_listesi_yeni) == len(urun_listesi):
        print(f"Bir hata oluştu: ID {urun_id} ile eşleşen bir ürün bulunamadı.")
    else:
        json_yaz(urun_listesi_yeni) # Güncellenmiş listeyi dosyaya yazarız.
        print(f"ID {urun_id} olan ürün başarıyla silindi.")
    
