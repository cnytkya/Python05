#Py'da for döngüsü belirli bir dizi(list,tuple,dize) içindeki her bir öğe üzerinde işlem yapmak için kullanılır.

# Aslında, döngüyü bir koleksiyondaki her bir elemanı ziyaret eden bir gezgin gibi düşünebilirsiniz.

"""
 -----------for döngüsü yapısı
for gezgin in koleksiyon
    yapılacak işlemler bu blokta gerçekleşir.

for: döngüyü başlatan kelime anahatarı.

gezgin(farklı isimler gelebilir): koleksiyondaki her bir elemanı ziyaret eder.

in: hangi koleksiyondan veri çekeceğimizi ifade eder. yani gezilecek koleksiyonun içinde olduğunu belirtir.

koleksiyon: Döngüye alınacak liste.
"""
sayilar = [1,2,3,4,5,6]
for sayi in sayilar:
    print("Sayılarımız: ",sayi)

# bir değişken tanımlayıp değişkene "python" değerini ata. for ile değeri gezip her bir harfi ayrı ayrı ekrana yazdıran console uygulmasını yazın.

name = "python"
for harf in name:
    print(harf)


# range() fonksiyonuyla döngü kurmak. belirli bir sayı aralığında işlem yapmak için range(aralık, 0 ile 100 arasında=> 0,100) fonksiyonu kullanılır. range(başlangıç,bitiş,adım)

#örnek: 0-4 sayıları yazdırma: varsayılan 0'dan başlar ve 1'er 1'er artar.
for i in range(5):
    print(i)

print("\n2'den başlayıp 10'kadar olan çift sayıları yazdıran console uygulaması")
#soru: 2'den başlayıp 10'kadar olan çift sayıları yazdıran console uygulamasını yazınız. 10 dahil olsun.
for sayi in range(2,11,2):
    print(sayi)

#tek ve çift sayılardan oluşan bir liste tanımlayın. for döngüsü kurarak çift olan sayıları toplayan console uygulamasını yazın.
print("\nÇift sayıları toplayan console uygulaması")
numbers = [2,4,5,8,12,3,10]
toplam = 0
for number in numbers:
    if number % 2 == 0:
        toplam = toplam + number

print("çift sayıların toplamı: ", toplam)

# 1'den 100'e kadar olan sayılardan 3'e ve 5'e tam bölünen sayıların toplamını bulan console uygulamasını yazın.
print("\n1'den 100'e kadar olan sayılardan 3'e tam bölünen sayıların toplamını bulan console uygulaması")

#adım 1: toplam değişkeni tanımla
toplam = 0

for sayi in range(1,101):
    if sayi % 3 == 0:
        # toplam = toplam + sayi
        toplam += sayi

#son döngüden sonra toplamı ekrana yazdıralım.
print("3'e tam bölünen sayıların toplamı: ",toplam)


