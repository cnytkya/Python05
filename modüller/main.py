#matematik modülünü buraya import etmemiz gerekir: Toplama,Çıkarma metotların hepsini tek seferde almak istersek aşağıdaki gibi import etmemiz gerekir
import matematik
import matematik as m
from matematik import carp,PI

#1.Yönetm: Modüldeki her şeyi kullanmak istersek.
#matematik modülündeki toplam fonksiyonunu kullanma
sonuc_toplam = matematik.toplam(15,20)
print(f"Toplam sonuç: {sonuc_toplam}")

#matematik modülündeki PI değişkenini kullanma
print("PI Sayısı",matematik.PI)

# Bu yöntemde, modülün içindeki elemanlara erişmek için "modül_adı.eleman_adı" şeklinde bir söz dizimi kullnamız gerekir.

#2.Yöntem: from ...import deyimi
#Eğer modülün içindeki belirli bir alanı,fonksiyonu veya değişkeni kullanmak istersek bu yöntem daha pratiktir.
sonuc_carpma = carp(8,2)#Carp metodunu direkt kullanma
print(f"Toplam sonuç: {sonuc_carpma}")

#PI sayısını direkt kullanma
print("PI Sayısı:",PI)

# as deyimi ile takma ad verme
sonuc_toplam = m.toplam(10,25)
print(f"as takısı ile Toplam sonuç: {sonuc_toplam}")