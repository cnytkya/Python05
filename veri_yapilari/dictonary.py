#Sözlükler(dict): anahtar:değer(key:value)
# sözlükler key ve value çiftlerinden oluşan, değiştirilebilir ve sırasız bir yapısı vardır. süslü parantez {} ile tanımlanır.

ogrenci_bilgileri = {
    "name" : "ahmet",
    "yas" : 25,
    "sinif" : "10-B"
}

#Soru: ekranda sadece ahmet bilgisini görmek istersek.
print(f"Öğrenci adı: {ogrenci_bilgileri["name"]}")
print(f"Öğrenci yaşı: {ogrenci_bilgileri["yas"]}")

#soru: listenin uzunluğunu veren kodu yazın.
#Beklediğimiz çıktı : Öğrenci bilgileri listesinin uzunluğu: 3
print(f"Öğrenci bilgileri listesinin uzunluğu: {len(ogrenci_bilgileri)}")

#anahtar:değer
print(ogrenci_bilgileri.items())

# sözlüğün değerlerini gösterme
print(ogrenci_bilgileri.values())

# sözlüğün anahtarları
print(ogrenci_bilgileri.keys())

