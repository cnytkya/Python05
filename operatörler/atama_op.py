# atama op: =

""" 
   = değer ataması x = 5 (x'e 5'i atadık)
   += toplayıp ata x += 5 (x'e 5 ekle sonra ata) => x = x + 5
   -= çıkarıp ata x -= 5 (x'ten 5 eksilt sonra ata) => x = x - 5
   *= çarpıp ata x *= 5 (x'i 5'e çarpıp sonra ata) => x = x * 5
   /= böl ata x /= 5 (x'i 5'e böl sonra ata) => x = x / 5
   %= mod al ata x %= 5 (x'in 5'e bölümünden kalanı ata) => x = x % 5
"""
x = 5
x += 3
print(x)

# Soru: bir sayının hem 3'e hem de 5'e tam bölünmesini kontrol eden python kodunu yaz.
num = 15
print((num %3 == 0) and (num %5 == 0)) #sonuç: true

# soru: kullanıcıdan alınan bir sayının 5'ten büyük veya küçük olduğunu kontrol eden console uygulamasını yaz.
number = int(input("Bir sayı giriniz: "))
print("\n5 haricindeki tüm sayılarda durum true olur.")
print(f"Durum: {(number > 5) or (number < 5)}") # 5 haricindeki tüm sayılarda durum true olur.