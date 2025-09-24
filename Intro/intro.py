#----------------Kısa Yollar----------------

#Yorum satırı için: AltGr + # ya da CTRL + ö
# Bir üst satırı alt satıra kopyalamak için: CTRL + D
# Bir satırı silmek için: pause + delete

#Aşağıdaki çıktıları python diliyle ekrana yazdıralım.
#1. Merhaba Dünya(doğrudan yazdırın)
#2. Selam Python dersine hoşgeldiniz(değişken kullanarak yazdırın)
#3. Ben 25 yaşındayım(değişken kullanarak yazdırın)


#1. Merhaba Dünya(doğrudan yazdırın)
print("Merhaba Dünya") # doğrudan yazdırma

#2. Selam Python, dersine hoşgeldiniz(değişken kullanarak yazdırın)
selam = "Selam," # burdaki değişken global bir değişkendir. yani mevcut sayfanın her yerinde kullanılabilir.
python11 = "Python dersine"
welcome = "hoşgeldiniz"
print(selam, python11, welcome)  # değişken kullanarak yazdırma
#Not: Bir çıktı(view) görmek istersek print() fonksiyonunu kullanırız.

#Değişken ve veri tipi nasıl tanımlanır?
# değişken = değer
degisken_adi = "değer" # string tipinde bir değişken tanımlama.
degisken_adi = 15 # int tipinde bir değişken tanımlama.
degisken_adi = 15.5 # float tipinde bir değişken tanımlama.

# Değişken ve veri tipleri: Değişkenler, programlama dillerinde verileri saklamak için kullanılır. Python'da değişkenler dinamik olarak tip alır. Bir değişken tanımlarken veri tipini belirtmemize gerek yoktur. Python, atanan değere göre değişkenin tipini otomatik olarak belirler.

#Ör
print("\nİki sayının toplamını hesaplayalım.") 
a = 10 # veri tipi int
b = 20
toplam = a + b # toplam değişkeni int tipinde
print("Toplam:", toplam) # çıktı: Toplam: 30

#iki sayının toplamını string format ile ekrana yazdıralım.
print("\nİki sayının çarpımını string format ile ekrana yazdıralım.")
x = 5
y = 10
carpim = x * y
print(f"x ve y'nin çarpımı: {carpim}")  # f-string ile string formatlama.

# soru: iki sayının bölümünden kalanını hesaplayalım.
print("\nİki sayının bölümünden kalanını hesaplayalım.")
sayi1 = 10
sayi2 = 2
bolum_kalan = sayi1 % sayi2
print(f"{sayi1} sayısının {sayi2} sayısına bölümünden kalan: {bolum_kalan:.2f}")  # .2f ile ondalık basamakları sınırlama.

# değişken tanımlamadan iki sayının bölümünden kalanını hesaplayalım.
print("\ndeğişken tanımlamadan iki sayının bölümünden kalanını hesaplayalım.")
print(f"10 sayısının 2 sayısına bölümünden kalan: {10 % 2:.2f}")  # doğrudan sayıları kullanarak hesaplama.

#1. toplama
a = 15
b =2
toplam = a + b
#2. Çıkarma
a = 15
b =2
cikarma = a - b
#3. Çarpma
a = 15
b =2
carpma = a * b
#4. bölme
a = 15
b =2
bolme = a / b
#5. Modülüs (kalan) - Mod alma
a = 15
b = 2
modulus = a % b

#Soru: Bir öğrencinin sınavdan aldığı 3 notu olsun. Bu notların ortalamasını hesaplayalım.Değişken tanımlayarak yapalım. Notlar: 85, 90, 78 
print("\nBir öğrencinin sınavdan aldığı 3 notun ortalamasını hesaplayalım.")
not1 = 85
not2 = 90
not3 = 78
ortalama = (not1 + not2 + not3) / 3
print(f"Öğrencinin not ortalaması: {ortalama:.2f}")  # .2f ile ondalık basamakları sınırlama.