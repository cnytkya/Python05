# Döngü, bilgisayara bir illemi tekrar tekrar yapmasını söyleyen yapıdır.

# örnek olarak, 1'den 5'e kadar olan sayıları ekrana yazdırmak istersek bunun en kısa yolu döngü içerisinde kullanmaktır.

"""while döngüsü yapısı
   while koşul:
       koşul sağlandığı sürece çalışacak kod bloğu.
   while (iken,--dığında...)
"""

#örnek: sayı 1'den büyük-eşit olduğu sürece kod bloğu çalışsın.

#sonsuz bir döngü örneği
# sayi = 1
# while sayi >=1:
#     print("Sayı 1'den büyük veya eşittir.")
#Not:  eğer biz müdahale etmezsek ekranda sonsuza kadar "Sayı 1'den büyük veya eşittir." yazar. bu işlem bilgisiyardaki geçici belleğimiz yani ram bellek dolana kadar devam eder.

sayi = 5
while sayi >=1:
    print("Sayı 1'den büyük veya eşittir.")
    sayi -= 1 # sayıyı bir azalttık ki sonsuz döngüden çıksın. sayi = sayi - 1

# kullanıcıdan bir sayı isteyelim, kullanıcı eğer 0'a basarsa program sonlansın. diğer durumlarda sürekli kullanıcıdan değer alan console app'i yazınız.

#1.Kullanıcıdan değer al
#2.Kullanıcının girdiği sayıyı kontrol et. Kullanıcının girdiğ sayı 0'dan farklıysa while döngüsüne girsin. kullanıcının girdiği değeri ekranda göster ve tekrar tekrar kullanıcıdan değer alıp koşulu kontrol et.
#3.eğer koşul sağlanmıyorsa(yani kullanıcı 0'a basarsa while döndüsünden çıkılsın)
sayi = int(input("Bir sayı giriniz: "))
while sayi != 0:
    print(f"Kullanıcının girdiği sayı: {sayi}")
    sayi = int(input("Bir sayı giriniz: "))
print("Program sonlandırıldı!!!")    







