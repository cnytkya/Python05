# Bir program yazarken bazen bir şeye karar vermemiz gerekir. örneğin hava yağmurlu mu kontrol et,eğer hava yağmurluysa şemsiyeni al gibi bir karar yapısı kurulur. Aşağıdaki örnekte olduğu gibi
yagmurlu = True
if yagmurlu: # eğer hava yağmurluysa
    print("Hava yağmurlu mutlaka şemsiyeni almalısın") #if sadece koşul doğruysa çalışır. if ingilizcede eğer demek.
else: # değilse(ya öyle ya da böyle)
    print("Hava yağmurlu değildir.")

#if-elif-else: elif "else if" (yani eğer değilse ve başka bir koşul varsa) birden fazla ihtimali kontrol etmemizi sağlar. 
"""if-elif-else yapısı
        if a:
            koşul sağlanırsa bu kod bloğu çalışır.
        elif b:
            alternif 1
        elif c:
            alternatif 2....
        else:
            eğer hiç biri değilse bu kod bloğu çalışır.
"""

# soru: not 75 olsun, buna göre eğer not 90 dan büyük veya eşitse "Çok iyi", eğer not 70'ten büyük-eşitse "İyi", eğer not 50'den büyük-eşitse "Orta", değilse "Zayıf" yazsın.
print("\n----------------------------------------------")
ogrenci_notu = 75
if (ogrenci_notu >=90) and (ogrenci_notu <= 100):
    print("Çok iyi")
elif ogrenci_notu >= 70:
    print("İyi")
elif ogrenci_notu >= 50:
    print("Orta")
else:
    print("Zayıf")

# harf notu uygulaması: Kullanıcıdan bir not girişi alınacak. Bu nota göre harf notu hesaplanacak.
# 90-100 -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# 0-59 -> F

ogrnc_notu = int(input("\nÖğrenci notunu giriniz: "))
if ogrnc_notu >=90 and ogrnc_notu <= 100:
    print("A")
elif ogrnc_notu >=80 and ogrnc_notu <= 89:
    print("B")
elif ogrnc_notu >=70 and ogrnc_notu <= 79:
    print("C")
elif ogrnc_notu >=60 and ogrnc_notu <= 69:
    print("D")
elif ogrnc_notu >=0 and ogrnc_notu <= 59:
    print("F")
else:
    print("Geçersiz not girişi")


