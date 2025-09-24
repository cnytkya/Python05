# python'da döngülerde (while,for) kullanılan özel anahtar kelimelerdir.

#1. break: kır,geç,çık anlamına gelir. bu komut döngüyü hemen sonlandırır. döngü şartı doğru olsa bile break gördüğü anda döngüden çıkar.

#2. contiune: O anki adımı atlar ve döngünün başına döner. yani contiune satırından sonraki çalışmaz, döngü kaldığı yerden devam eder.

#break örneği
        #s1,s2,s3,s4,s5,s6,s7
sayilar = [1,2,3,4,5,6,7] # s burdaki elemanları tek tek gezer ve nihaytinde bunları ekranda göstermek bellekte tutar. (s=gezgin)
for s in sayilar:#eğer s 5'e gelirse döngü sonlansın. bunun için break komutunu kullanırız.
    if s == 5:
        print("5 görüldü, döngüden çıkılıyor.")
        break
    print(s) #1,2,3,4
print("\n--------------------------------------------------")
#continue örneği
for gezgin in sayilar:
    if gezgin == 4: 
        print("4 atlandı")
        continue  # ben 4 ü görmek istemezsem
    print(gezgin)

# while ile örnek(break + continue)
print("\n--------------------------------------------------")

sayac = 0
while True:# burda true yani her şartte while bloğuna girer.
    sayac +=1
    if sayac == 3:
        print("3 atlandı")
        continue
    if sayac == 7:
        print("7 bulundu, döngü kırıldı(break)")
        break # döngü tamamen sonlanır.
    print("Sayı: ", sayac)
print("Döngü sonlanmıştır. Programı yeniden çalıştır.")

#Özet
# break -> Döngüyü tamamen sonlandırır.
# continue -> sadece o adımı atlar, döngü devam eder.

# Şifre Giriş Uygulaması: şifre doğru girilince break ile çıkış, yanlış girişte continue ile tekrar deneme şeklinde yazalım. while döngüsünde kullanıcı doğru şifreyi yazana kadar döngü devam etsin, eğer kullanıcı doğru şifreyi girerse while döngüsü sonlansın.

sifre = "123"
while True:
    password = input("Şifreyi giriniz: ")

    if password == "":
        print("Boş şifre girdiniz, tekrar deneyiniz(continue)")
        continue
    if password == sifre:
        print("Şifre doğru girilmiştir")
        break
    else:
        print("Yanlış şifre, tekrar deneyiniz.")









