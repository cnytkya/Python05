#Karar yapıları (If-Else): If-Else yapıları, programın belirli koşullara göre farklı yollar izlemesini sağlar. Hava durumuna göre şemsiye ya da şapka alma durumunu if-else ile yapılabilir.

#Kullanıcıdan değer alma. 
# sayi = int(input("Bir sayı giriniz: ")) #int tipinde değer alma
# name = input("Adınızı giriniz: ") #string tipinde değer alma
# onadlik = float(input("Ondalık bir sayı giriniz: ")) #float tipinde değer alma.

#Algoritma sorusu: Sayı çift mi tek mi?
# 1.Kullanıcıdan bir sayı iste.
# sayi = int(input("Bir sayı giriniz: "))
# # # 2.Kullanıcıdan aldığımız sayının çift mi tek mi olduğunu kontrol et.
# if sayi % 2 == 0: #eğer sayı tam bölünüyorsa "sayı çifttir" yazsın
#     print("Sayı çifttir.")
# else: #eğer tam bölünmüyorsa "sayı tektir" yazsın
#     print("Sayı tektir.")

#Bir sayının pozitif mi negatif mi olduğunu kontrol etme.
#1.Kullanıcıdan bir sayı iste.
# sayi = int(input("Bir sayı giriniz: "))
# #2.Sayı 0'dan büyükse "pozitif" değilse "negatif" yazsın.

# if sayi > 0: #sayı 0'dan büyükse
#     print("Sayı pozitif.")
# else: #sayı 0'dan küçükse
#     print("Sayı negatif.")

# 2 sayının toplamının çift mi tek mi olduğunu kontrol etme.
#1.Farklı iki sayı tanımla.
# s1 = 12
# s2 = 8
# #2.Sayıların toplamını hesapla.
# toplam = s1 + s2
# #3.Toplam çift mi tek mi kontrol et.
# if toplam % 2 == 0:
#     print("Toplam çift sayıdır.")
# else:
#     print("Toplam tek sayıdır.")

#Ehliyet alma kontrolü algoritması:
# Kullanıcıdan yaşını alın.
yas = int(input("Yaşınızı giriniz: "))
# Eğer yaş 18 veya daha büyükse "Ehliyet alabilirsiniz" yazdırın.
if yas >= 18:  # Eğer yaş 18 veya daha büyükse
    print("Ehliyet alabilirsiniz.")

# Aksi halde "Ehliyet almak için yaşınız tutmuyor" yazdırın.
else:  # Eğer yaş 18'den küçükse
    print("Ehliyet almak için yaşınız tutmuyor.")

