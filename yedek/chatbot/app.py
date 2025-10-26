# session'ı ve redirect'i (yönlendirme) içe aktarıyoruz
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# --- GÜVENLİK UYARISI ---
# Session (oturum) kullanmak için BU ANAHTAR ZORUNLUDUR.
# Gerçek bir uygulamada bunu 'cok_gizli_bir_sey' gibi basit bir şey yapmayın.
# Rastgele ve uzun bir dize kullanın.
app.secret_key = 'ogrenci_projesi_icin_gizli_anahtar_12345'


# --- Chatbot Mantığı Fonksiyonumuz (Sözlük Versiyonu) ---
CEVAP_KURALLARI = {
    "merhaba": "Selam! Sana nasıl yardımcı olabilirim?",
    "nasılsın": "Ben bir programım, harika hissediyorum! Sen nasılsın?",
    "adın ne": "Bana 'Yardımcı Bot' diyebilirsin.",
    "hava nasıl": "Üzgünüm, hava durumunu bilemiyorum. Ben basit bir botum.",
    "görüşürüz": "Görüşmek üzere, kendine iyi bak!",
    "çıkış": "Görüşmek üzere, kendine iyi bak!",
    "teşekkürler": "Rica ederim! Başka bir sorun var mı?"
}

def chatbot_cevabi_al(kullanici_mesaji):
    mesaj = kullanici_mesaji.lower()
    for anahtar_kelime, cevap in CEVAP_KURALLARI.items():
        if anahtar_kelime in mesaj:
            return cevap
    return "Üzgünüm, dediğini tam olarak anlayamadım."
# ----------------------------------------------------


@app.route('/', methods=['GET', 'POST'])
def ana_sayfa():
    # 1. Eğer session'da 'chat_gecmisi' adında bir liste yoksa, oluştur.
    # Bu, kullanıcının siteyi ilk kez açtığı anlamına gelir.
    if 'chat_gecmisi' not in session:
        session['chat_gecmisi'] = [] # Boş bir liste başlat

    # 2. Eğer kullanıcı formu gönderdiyse (POST)
    if request.method == 'POST':
        # 3. Mesajı al
        kullanici_mesaji = request.form['mesaj_kutusu']
        
        # 4. Botun cevabını al
        bot_cevabi = chatbot_cevabi_al(kullanici_mesaji)
        
        # 5. Hem kullanıcının mesajını hem de botun cevabını session'daki listeye ekle
        # (Daha net görünmesi için sözlük olarak ekleyelim)
        session['chat_gecmisi'].append({'kisi': 'Siz', 'mesaj': kullanici_mesaji})
        session['chat_gecmisi'].append({'kisi': 'Bot', 'mesaj': bot_cevabi})
        
        # session listesini güncellediğimizi belirtmemiz gerekebilir
        session.modified = True 

        # 6. Sayfanın yeniden POST edilmesini önlemek için ana sayfaya geri YÖNLENDİR (redirect)
        # Bu, sayfa yenilendiğinde formun tekrar gönderilmesini engeller (PRG Deseni)
        return redirect(url_for('ana_sayfa'))

    # 7. Eğer kullanıcı sayfayı sadece açtıysa (GET) veya yönlendirildiyse:
    # Session'daki tüm sohbet geçmişini al
    gecmis_konusmalar = session.get('chat_gecmisi', [])
    
    # 8. HTML şablonunu bu geçmişle birlikte oluştur
    return render_template('index.html', gecmis=gecmis_konusmalar)


# BONUS: Sohbeti temizlemek için bir rota
@app.route('/temizle')
def temizle():
    # Session'daki sohbet geçmişini temizle
    session.pop('chat_gecmisi', None) 
    # Ana sayfaya yönlendir
    return redirect(url_for('ana_sayfa'))


# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)