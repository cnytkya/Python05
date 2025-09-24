# Operatörler, bilgisayara bir işlem yapmasını söyleyen işaretlerdir. 
# Günlük hayatta +,-,x,/ gibi matematik işaretlerini kullanırız. Python'da benzer işaretler kullanılır.

"""
ör ;toplama (+): 5 + 5 = 10 
    çıkarma (-)
    çarpma (*)
    bölme (/) => ondalık kısımları gözükür
    tam bölme (//) => tam bölme yani ondalık kısım gözükmez.
    kalan(mod) (%)
    üs alma (**)

"""
print("Toplama")
a = 5
b = 8
toplam = a + b
print(f"a + b = {toplam}")

print("\n------------------------------------\nÇıkarma")
a = 3
b = 2
cikarma = a - b
print(f"a - b = {cikarma}")
print("\n------------------------------------\nÇarpma")
a = 3
b = 9
carpma = a * b
print(f"a * b = {carpma}")

print("\n------------------------------------\nBölme")
a = 12
b = 5
bolme = a / b
print(f"a / b = {bolme}")

print("\n------------------------------------\nTam Bölme")
a = 12
b = 5
tam_bolme = a // b
print(f"a // b = {tam_bolme}")

print("\n------------------------------------\nMod alma(kalanı bulma)")
a = 120
b = 7
mod_alma = a % b
print(f"a // b = {mod_alma}")