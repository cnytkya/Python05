#aylık yol masrafı hesaplama uygulaması: Bu uygulama, kullanıcının girdiği verilere göre aylık yakıt masrafını hesaplar. 

# Python'da fonksiyon tanımlamak için def kelime anahtarı kullanılır. fonksiyon adı genellikle küçük karakterlerle ve eğer iki kelime ve üzeri ise alt çizgi(_) kullanılır.

def aylik_masfraf_hesapla():
    """Kullanıcıdan aylık yolculuk bilgilerini alarak toplam yakıt maliyetini hesaplayan fonksiyon.
    """
    print("Aylık Yol Masrafı Hesaplama Uygulamasına Hoşgeldiniz\n-------------------------" )

    #try-except
    try:
        #kullanıcıdan km cinsinden yolculuk mesafesini alalım.
        mesafe_km = float(input("Lütfen aylık toplam yolculuk mesafenizi(km) giriniz: "))
        #kullanıcıdan yakıtın litre fiyatını alalım.
        litre_fiyat = float(input("Lütfen kullandığınız yakıtın litre fiyatını(TL) giriniz: "))
        #kullanıcıdan her 100 km de ne kadar yakıt yaktığını alalım.
        yakit_100km_tuketimi = float(input("100 km'deki yakıt tüketimini giriniz: "))

        #toplam yakıt tüketimi al
        # 1 km'de ne kadar yakıt tükketiğini bul
        toplam_yakit_tuketimi = (mesafe_km / 100) * yakit_100km_tuketimi

        #toplam gideri hesapla
        toplam_gider = toplam_yakit_tuketimi * litre_fiyat
        #sonuçlar
        print("\n------------------Sonuçlar--------------------")
        print(f"Aylık ortalama yakıt tüketiminiz: {toplam_yakit_tuketimi} litre")
        print(f"Aylık ortalama masrafınız: {toplam_gider} litre\n")
        print("----------------------------------------------\n")
    except ValueError:
        #kullanıcı sayı yerine farklı karakter girerse değer hatası fırlatalım.
        print(f"Lütfen sayısal değerler girin")
    except Exception as hata:
        print("Bir hata oluştu: ", hata)


aylik_masfraf_hesapla()
    


