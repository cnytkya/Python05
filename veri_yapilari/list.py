#list: list veri tipi birden fazla değeri bir arada tutar.

# Elemanların sıralı ve değiştirilebilir(mutable) koleksiyonlardır. 

#Köşeli parantez [] ile oluşturulur.

# str listesi
meyveler = ["elma","muz","kiraz","armut","avakado"]
# sayı listesi
sayilar = [1,2,7,5,2,8,8]

# farklı veri tiplerini barındıran list
karisik_liste = ["elma",12,15.5,True]

# print(karisik_liste)

arabalar = ["bmw","renault","honda","fiat","audi"]
# soru: ekranda sadece renault çıktısını veren kodu yazın.
#print(arabalar[1]) #renault çıktısını verir.

# indexleme: bir listenin herhangi bir elemanına erişmek için indexleme yapılır. indexleme, 0'dan başlayarak devam eder. listenin ilk elemanı index 0'a denk gelir. 

# 0.index: bmw
# 1.index: renault => ekranda gösterilecek eleman.
# 2.index: honda
# 3.index: fiat
# 4.index: audi

#eleman güncelleme
teknolojik_aletler = ["telefon","kulaklık","pc","powerbank","drone"]
#soru: "pc" elemanını "bilgisayar" olarak güncelleyin.
teknolojik_aletler[2] = "bilgisayar"
# print(teknolojik_aletler)

# Liste Metotları: append(), insert(), remove(),pop(),sort(),len() vs.

#1.append()
newList = ["elma","armut","üzüm","bamya","domates"]
#listenin sonuna "kivi" ekleyelim.
newList.append("kivi")
print("yen liste: ", newList)
# print(f"yen liste: {newList}") #format kullanarak
#2.insert
sayilar = [1,2,3,4]
#sayilar listesinin 1 ve 2 arasına 0 rakamanı koyalım.
sayilar.insert(1,0) #ikinci pozisyona 0 ekle.

#3.remove() func.
# sayilar listesinden 3 adındaki elamanı kaldıralım.
sayilar.remove(3)
print(sayilar)

#4.pop() func.
son_elaman = sayilar.pop() #listenin son elemanını çıkarır.
# print(son_elaman)
# print(sayilar)

# sort() func.
sayilar2 = [4,5,6,62,22]
sayilar2.sort()
print(sayilar2)

# len() func.
# bir listenin uzunluğunu hesaplar.
print(len(sayilar2)) # çıktı: 5

# slicing(liste dilimleme)
#Listenin belirli bir kısmını ekrana yazdıralım.
numbers = [45,20,66,88,21,33]
#soru: numbers listesinin sadece 20,66 ve 88 elemanlarını ekrana yazdırmak istersek.
print(f"slicing ile istenilen parçayı alma: {numbers[1:4]}")
