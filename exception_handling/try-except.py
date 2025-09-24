# python try-except yapısı, hataları(exceptions) yakalamak ve yönetmek için kullanılır. Hata durumlarını yönetmek programın bir anda kapanmasını engelleyebiliriz. Eğer bu yapıyı kurmazsak ve bir hata oluştuğunda program sonlanır.

#Temel Yapı
"""
try:
    #hata oluşturabilecek kodlar buraya gelecek.
    #çalışmasını istediğimiz yer burasıdır.
except hatatürü:
    #eğer hata varsa bu kod bloğu çalışacak.

"""

#Basit örnek
#Kullanıcıdan sayı isteyelim. eğer kullanıcı harf girerse ValueError oluştursun.
"""
try:
    # number = int(input("Bir sayı giriniz: "))
    number = float(input("Bir sayı giriniz: "))
    # print("Girdiğiniz sayı: ", number)
    print(f"Girdiğiniz sayı: {number}")
except ValueError:
    print("Giridiğiniz değer sayı türünde değildir.")
"""

#birden fazla exception fırlatma
"""
try:
    bolunen = int(input("Bölünen sayıyı gir: "))
    bolen = int(input("bölen sayıyı gir: "))
    sonuc = bolunen / bolen
    print("Sonuç: ", sonuc)
except ValueError:
    print("Buraya sadece sayı girilebilir!")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez!")
"""
# try içerisinde bir liste oluşturalım. print hatalı bir index tanımlaması yapalım ve excep olarak "Bir hata oluştu" yazdıralım.

"""
try:
    liste = [1,2,3]
    print(liste[5]) # hatalı index
except:
    print("Bir hata oluştu.")
"""

# as ile hata detayını görmek
"""
try:
    x = int("abc")
except ValueError as hata:
    print("hata oluştu",hata)
"""
#bölme işlemi uygulaması
def bolme_islemi():
    try:
        a = float(input("Pay: "))
        b = float(input("Payda: "))
        result = a / b
    except ZeroDivisionError:
        print("Sıfıra bölme hatası")
    except ValueError:
        print("Geçersiz değer. Lütfen sayı girmeye çalışın.")
    else:
        print("Sonuç: ",result)
    finally:#finally her türlü çalışacak kod bloğudur.
        print("Fonksiyon tamamlandı.")

bolme_islemi()
