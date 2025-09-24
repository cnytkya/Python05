# product management : Ürün Yönetim Uygulaması.
# ürün eklenirken ya da silinirken otomatik olarak json dosyası bir kere oluşsun. 
# Bu uygulamada kullanılacak kütüphaneler: 
# json dosyalarıyla çalışırken "json" kütüphanesini kullanabiliriz. 
# işletim sistemi ile ilgili işlemler için "os" kütüphanesini kullanabiliriz (dosya kontrol,ekran temizleme,yeni dosya oluşturma,dosya silme). 
# hangi işletim sistemi kullanıldığını öğrenmek için "platform" adlı kütüphaneyi kullanabiliriz.
import json
import os
import platform

#Ürünlerin saklanacağı json dosyasının adı
DATA_FILE = "products.json"

# JSON dosyasını yükleyecek metot
def load_data():
    # eğer dosya yoksa boş bir liste döndür
    if not os.path.exists(DATA_FILE):
        return []
    # Dosya varsa dosyayı okuma modunda aç ve JSON içeriğini yükle.
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


#JSON dosyasına kaydet
def save_data(products):
    # dosyayı yazma modunda aç ve ürün listesini JSON formatında kaydet.
    with open(DATA_FILE, "w", encoding= "utf-8") as f:
        json.dump(products, f , indent=4)

#konsole temizleme fonksiyonu
def clear_screen():
    #işletim sistemi windows ise "cls" komutunu çalıştır.
    if platform.system() == "Windows":
        os.system("cls")
    else:# Linux veya Mac ise "clear" komutunu çalıştır.
        os.system("clear")

#Ürünleri listeleme fonksiyonu
def list_products(products):
    #Eğer ürün listesi boş ise
    if not products:
        print("Henüz ürün yok!")
    else:
        #Listedeki her ürün için bilgileri ekrana yazdır.
        for p in products:
            print(f"ID: {p['id']} | Ad: {p['name']} | Fiyat: {p['price']} | Stok: {p['stock']}")

#Ürün ekleme fonksiyonu
def add_product(products):
    #Ürün eklenirken id'yi otomatik bir bir artır.
    product_id = len(products) + 1
    name = input("Ürün Adı: ")
    price = float(input("Fiyat Girin: "))
    stock = int(input("Ürün Adedi: "))

    product = {
        "id": product_id,
        "name":name,
        "price":price,
        "stock":stock
    }
    #Ürünü listeye ekle.
    products.append(product)
    #Güncel listeyi dosyaya kaydet
    save_data(products)
    print("Ürün eklendi")

#Ürün güncelleme fonksiyonu
def update_product(products):
    # Önce mevcut listeyi ekranda göster
    list_products(products)
    #Kullanıcıdan güncellenecek ürünün id'sini iste
    pid = int(input("Güncellenecek ürün ID: "))
    #Ürünleri kontrol et
    for p in products:
        if p["id"] == pid: #ID eşleşirse
            # Kullanıcı name için değişiklik yaparsa "new_name" oluşturulsun, diğer durumda eski "name" korunsun.
            p["name"] = input(f"Yeni Adı: ({p["name"]}): ") or p["name"]
            try:
                #Yeni fiyat bilgisini kullanıcadan al. Boş bırakılırsa eski fiyatı koru.
                p["price"] = float(input(f"Yeni Fiyat ({p["price"]}): ")) or p["price"]
                #Yeni stok bilgisini kullanıcadan al. Boş bırakılırsa eski stok korunsun.
                p["stock"] = int(input(f"Yeni Stok ({p["stock"]}): ")) or p["stock"]
            except ValueError:
                print("Sayısal değer girmeniz gerekiyor. Güncelleme iptal edildi!")
                return
            # Güncelleme işleminden sonra listeyi son haliyle uygula
            save_data(products)
            print("Ürün başarıyla güncellendi")
            return
        #eğer ID bulunmazsa uyarı ver.
        print("Ürün bulunamadı!!!")

#Silme fonksiyonu
def delete_p(products):
    #Önce listeyi yükle
    list_products(products)
    #Kullanıcıdan silinecek ürün ID'si iste
    pid = int(input("Silmek istediğin ürün ID: "))
    #Listeden ilgili ürünü çıkart(ID'si eşleşmeyenleri bırak)
    products = [p for p in products if p["id"] != pid]
    #Güncel listeyi kaydet.
    save_data(products)
    print("Ürün başarıyla silindi.")
    return products # Güncellenmiş listeyi geri döndür.

#Bir tane ana metot oluşturup, uygulama ilk çalıştığında bu ana metot yüklensin.
def main():
    #Program başladığında önce ürünleri yükle
    products = load_data()
    
    while True:
        #menü seçenekleri yazdır.
        print("\n-------Ürün Yönetim Uygulaması---------")
        print("1 - Ürünleri Listele")
        print("2 - Ürün Ekle")
        print("3 - Ürün Güncelle")
        print("4 - Ürün Sil")
        print("5 - Ekranı Temizle")
        print("0 - Çıkış")

        #kullanıcıdan seçim al
        choice = int(input("Seçim: "))

        if choice == 1:
            list_products(products)
        elif choice == 2:
            add_product(products)
        elif choice == 3:
            update_product(products)
        elif choice == 4:
           products = delete_p(products)
        elif choice == 5:
            clear_screen()
        elif choice == 0:
            print("Çıkış yapılıyor!")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyiniz.")

#Program çalıştığında ilk çağrılan kısım burası
if __name__ == "__main__":
    main()