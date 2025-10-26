from flask import Flask, render_template, request, session, redirect, url_for

#Bir flask uygulaması başlatalım

app = Flask(__name__)

#-----güvenlik uyarısı---------
# session(oturum) kullanmak için bu anahtar zorunludur.
app.secret_key = 'ogrenci_app_icin_cok_gizli_anahtar_12345'

CEVAP_KURALLARI = {
    "merhaba" : "Merhaba! Sana nasıl yardımcı olabilirim?",
    "selam" : "Selam! Sana nasıl yardımcı olabilirim?",
    "nasılsın" : "Ben bir programım, kendimi iyi hissediyorum! Sen nasılsın",
    "adın ne" : "Bana 'Yardımcı Bot' diyebilirsin",
    "bugün hava nasıl" : "Üzgünüm, hava durumunu bilmiyorum. Ben basit bir botum",
    "çıkış" : "Görüşmek üzere, kendine cici bak.",
    "görüşürüz" : "Görüşmek üzere, kendine cici bak.",
    "teşekkürler" : "Rica ederim! Başka bir sorun var mı?"
}
#-------chatbot mantığı fonksiyonu-------
def chat_bot_cevap_al(kullanici_mesaji):
    mesaj = kullanici_mesaji.lower()
    for anahtar_kelime, cevap in CEVAP_KURALLARI.items():
        if anahtar_kelime in mesaj:
            return cevap
    return "Üzgünüm, dediğini tam olarak anlayamadım"

    
#ana sayfamız için rota
# hem get(sayfayı ilk açma) hem de post(form gönderme) metotlarına izin veriyoruz.

@app.route('/',methods=['GET', 'POST'])

def ana_sayfa():

    # eğer session'da 'chat_gecmisi' adında bir liste yoksa, oluştur
    #bu kullanıcının siteyi ilk kez açtığı anlamına gelir.
    if 'chat_gecmisi' not in session:
        session['chat_gecmisi'] = [] #boş bir liste başlat

    #eğer kullanıcı formu gönderdiyse(POST işlemiyse)
    if request.method == 'POST':
        #HTML'deki 'mesaj_kutusu' adlı inputtan veriyi al.
        kullanici_mesaji = request.form['mesaj_kutusu']
        #bu mesajı chatbot fonk.muza gönderip cevabı al
        bot_cevabi = chat_bot_cevap_al(kullanici_mesaji)
        #hem kullanıcının mesajını hem de botun cevabını session'daki listeye ekle
        session['chat_gecmisi'].append({'kisi':'Siz', 'mesaj':kullanici_mesaji})
        session['chat_gecmisi'].append({'kisi':'Bot', 'mesaj':bot_cevabi})
        #session listesini güncellediğimizi belirtmemiz gerekebilir.
        session.modified = True
        #sayfanın yeniden POST edilmeisni önlemek için ana sayfaya geri yönlendir(redirect). bu sayfa yenilendiğinde formun tekrar gönderilmesini engeller.
        return redirect(url_for('ana_sayfa'))
    
    #sohbet gemişini al
    gecmis_sohbetler = session.get('chat_gecmisi', [])
    # HTML şablonu bu geçmişle birlikte oluştur

    return render_template('index.html', gecmis = gecmis_sohbetler)

#sohbeti temizlemek için bir rota
@app.route('/temizle')
def temizle():
    #session'daki sohbet geçmişini temizle
    session.pop('chat_gecmisi', None)
    return redirect(url_for('ana_sayfa'))


#Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)



