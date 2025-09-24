#dosyalarla çalışırken python bazı yerel kütüphanlerinden yararlanırız. farklı bir kütüphane seçecek olursa "pip install kütphane_adi" yazarak aynı işi harici bir kütüphaneyle yapabiliriz.

import json #Dataları kaydedebileceği/okuyabileceği JSON formatında dosyalar oluşturur. 
import os # Ekranı temizlemek için(cls,clear)

#öğrencilerin kaydedileceği dosya adı
DATA_FILE = "students.json"

# Ekranı temizlemek için metot.
def clear_screen():
    """
    İşletim sistemlerine ekranı temizleme karar yapısı
    """
    os.system("cls" if os.name == "nt" else "clear")

def load_data():
    """
    JSON dosyasından öğrenci verilerini yükler.
    Eğer dosya yoksa boş liste döner.
    """
    if not os.path.exists(DATA_FILE):#dosya mevcut değilse
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f) #JSON'ı liste olarak yükle.
    except:
        return [] #hata durumunda boş liste dön.
def save_data(students):
    #öğrenci listesini JSON dosyasına kaydeder.
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f,ensure_ascii=False, indent=2)

#mantık olarak eğer listede eleman yoksa null döner. listede zaten eleman yoksa ilk kayıt ID'si en küçüktür. ID bulunur ve bir fazlasını dönmesini bekleriz. eğer hiç öğrenci yoksa ve yeni bir kayıt oluşacaksa bunu 1'den başlatması gerekir. id'nin bir bir artma fonksiyonu algoritması.
def next_id(students):
    """
    Öğrencilerdeki en yüksek ID'yi bulur ve bir fazlasını döner. Eğer hiç öğrenci yoksa 1'den başlar.
    """
    if not students:
        return 1
    return max(s["id"] for s in students) + 1

def list_students(students):
    """
    Öğrencilerin listesini ekrana yazdırır.
    """
    #eğer öğrenci yoksa 
    if not students:
        print("Kayıtlı öğrenci bulunamadı")
        return
    print("\nId | Adı | Soyadı | Yaş | Bölüm | Ortalama")
    print("-"*50)
    for s in students:
        print(f"{s['id']} | {s['first_name']} | {s['last_name']} | {s['age']} | {s['department']} | {s['gpa']}")

#Öğrenci ekleme
def add_student(students):
    """
    Kullanıcıdan öğrenci bilgilerini alır ve listeye ekler.
    Daha sonra jshon dosyasına kaydeder.
    """
    print("===Yeni Öğrenci Ekle===")
    #Kullanıcıdan bilgileri alıyoruz.
    first = input("Adı: ")
    last = input("Soyadı: ")
    age = int(input("Yaşı: "))
    dep = input("Bölüm: ")
    gpa = float(input("Ortalama: "))

    students.append({
        "id":next_id(students),
        "first_name":first,
        "last_name":last,
        "age":age,
        "department":dep,
        "gpa":gpa
    })
    save_data(students)
    print("Öğrenci eklendi.")
#CRUD: Create,Read(listele),Update(güncelleme),Delete
#Öğrenci silme
def delete_student(students):
    """
    GetById => kullanıcıyı id'sine göre alır ve siler. Daha sonra save change uygular yani kayıt silindikten sonra json dosyasını son haliyle günceller.
    """
    sid = int(input("Silinecek Öğrenci ID: "))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data(students)
            print("Öğrenci silindi")
            return
    print("Öğrenci bulunamadı!")

#program başlarken öğrenci verilerini dosyadan yükle
students = load_data()

while True:
    #Menü ekranı
    print("\n=== Öğrenci Yönetim Uygulaması ===")
    print("1- Listele")
    print("2- Ekle")
    print("3- Sil")
    print("4- Ekranı Temizle")

    #kullanıcının seçim yapmasını sağla
    choice = input("Seçiminiz: ")
    #Seçime göre işlem yapılsın
    if choice == "1":
        list_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        delete_student(students)
    elif choice == "4":
        clear_screen()
    elif choice == "0":
        print("Çıkış yapılıyır...")
        break
    else:
        print("Geçersiz seçim!")

