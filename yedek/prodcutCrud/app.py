from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Veritabanı yerine geçici olarak hafızada bir liste kullanalım
products = [
    {"id": 1, "name": "Laptop", "price": 2500.00},
    {"id": 2, "name": "Mouse", "price": 150.00},
]
# Yeni eklenecek ürünler için ID sayacı
# Normalde bunu veritabanı otomatik yapar
g_product_id_counter = 3

# Helper function: ID'ye göre ürünü bul
def find_product_by_id(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

# --- CREATE ---
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        global g_product_id_counter
        # Formdan verileri al
        name = request.form['name']
        price = float(request.form['price'])
        
        # Yeni ürünü oluştur
        new_product = {
            'id': g_product_id_counter,
            'name': name,
            'price': price
        }
        
        # Listeye ekle ve sayacı artır
        products.append(new_product)
        g_product_id_counter += 1
        
        # Ana sayfaya yönlendir
        return redirect(url_for('index'))
    
    # GET request ise formu göster
    return render_template('add_product.html')

# --- READ (List All) ---
@app.route('/')
def index():
    # Tüm ürünleri ana sayfada listele
    return render_template('index.html', products=products)

# --- UPDATE ---
@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    # Güncellenecek ürünü bul
    product = find_product_by_id(product_id)
    
    if not product:
        return "Product not found", 404

    if request.method == 'POST':
        # Formdan gelen yeni verilerle ürünü güncelle
        product['name'] = request.form['name']
        product['price'] = float(request.form['price'])
        return redirect(url_for('index'))
    
    # GET request ise, mevcut verilerle dolu formu göster
    return render_template('edit_product.html', product=product)

# --- DELETE ---
@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = find_product_by_id(product_id)
    
    if product:
        products.remove(product)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)