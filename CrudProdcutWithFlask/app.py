import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

# Flask uygulamasını başlat
app = Flask(__name__)

# Veritabanı dosyasının adı
DATABASE = 'products.db'

# --- Veritabanı Bağlantı Fonksiyonları ---

def get_db():
    """
    İstek (request) başına bir veritabanı bağlantısı açar.
    Eğer bağlantı zaten varsa, mevcut olanı döndürür.
    'g' objesi, tek bir istek süresince global verileri saklamak için kullanılır.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Sonuçların 'dict' (sözlük) gibi erişilebilir olmasını sağlar
        # Örn: product['name'] şeklinde
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    """
    İstek (request) sona erdiğinde (başarılı veya hatalı)
    veritabanı bağlantısını otomatik olarak kapatır.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """
    'schema.sql' dosyasını okuyarak veritabanı tablolarını oluşturur.
    Bu fonksiyonu projeyi ilk kez çalıştırırken manuel olarak tetikleyeceğiz.
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print("Veritabanı ve 'products' tablosu başarıyla oluşturuldu.")

# --- Yardımcı Fonksiyon ---

def get_product(product_id):
    """
    Verilen ID'ye sahip ürünü veritabanından çeker.
    Bulamazsa None (boş) döndürür.
    """
    db = get_db()
    product = db.execute(
        'SELECT * FROM products WHERE id = ?', (product_id,)
    ).fetchone()
    return product

# --- Rotalar (CRUD İşlemleri) ---

# R: Read (Listeleme - Ana Sayfa)
@app.route('/')
def index():
    """
    Tüm ürünleri veritabanından çeker ve 'index.html' şablonuna gönderir.
    """
    db = get_db()
    products_cursor = db.execute('SELECT * FROM products ORDER BY id')
    products = products_cursor.fetchall()
    return render_template('index.html', products=products)

# C: Create (Oluşturma)
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    """
    GET isteği: Yeni ürün ekleme formunu ('add_product.html') gösterir.
    POST isteği: Formdan gelen verileri alır ve veritabanına ekler.
    """
    if request.method == 'POST':
        # Formdan verileri al
        name = request.form['name']
        price = float(request.form['price'])
        
        # Veritabanına INSERT (Ekleme) sorgusu
        db = get_db()
        db.execute(
            'INSERT INTO products (name, price) VALUES (?, ?)',
            (name, price)
        )
        db.commit() # Değişiklikleri veritabanına kaydet
        
        # Ekleme sonrası ana sayfaya yönlendir
        return redirect(url_for('index'))
    
    # GET isteği ise (sayfa ilk açıldığında) formu göster
    return render_template('add_product.html')

# U: Update (Güncelleme)
@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    """
    GET isteği: ID'si verilen ürünün bilgilerini bulur ve 'edit_product.html' 
                 formunda dolu olarak gösterir.
    POST isteği: Formdan gelen yeni verilerle ürünü günceller.
    """
    # Önce güncellenecek ürünü veritabanından bul
    product = get_product(product_id)
    if product is None:
        return "Ürün bulunamadı", 404
    
    if request.method == 'POST':
        # Formdan yeni verileri al
        name = request.form['name']
        price = float(request.form['price'])
        
        # Veritabanında UPDATE (Güncelleme) sorgusu
        db = get_db()
        db.execute(
            'UPDATE products SET name = ?, price = ? WHERE id = ?',
            (name, price, product_id)
        )
        db.commit() # Değişiklikleri kaydet
        
        # Güncelleme sonrası ana sayfaya yönlendir
        return redirect(url_for('index'))
    
    # GET isteği ise (sayfa ilk açıldığında) formu ürün bilgileriyle dolu göster
    return render_template('edit_product.html', product=product)

# D: Delete (Silme)
@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """
    ID'si verilen ürünü veritabanından siler.
    Bu işlem sadece POST isteği ile tetiklenir (güvenlik için).
    """
    # Silinecek ürünün varlığını kontrol et
    product = get_product(product_id)
    if product is None:
        return "Ürün bulunamadı", 404
        
    # Veritabanından DELETE (Silme) sorgusu
    db = get_db()
    db.execute('DELETE FROM products WHERE id = ?', (product_id,))
    db.commit() # Değişiklikleri kaydet
    
    # Silme sonrası ana sayfaya yönlendir
    return redirect(url_for('index'))

# Uygulamayı çalıştırma bloğu
if __name__ == '__main__':
    # Not: init_db() fonksiyonunu çalıştırmayı unutmayın (Adım 5)
    app.run(debug=True)