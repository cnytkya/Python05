from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

#Veritabanı yerine geici olarak hafızada bir liste kullanalım

prdocucts = [
    {
        "id":1, "name":"Laptop","price":2500.00,
        "id":2, "name":"Mause","price":500.00,
    }
]

# Yeni eklenecek ürünler için ID sayacı. Eğer veritabanı olsaydı bunu otomatik yapardı.
g_prodcut_id_counter = 3

#id ye göre ürün bulma

def find_prodcut_by_id(prdocut_id):
    for product in prdocucts:
        if product['id'] == prdocut_id:
            return product
    return None


#CRUD - Create
@app.route('/add', methods = ['GET','POST'])

def add_prpduct():
    if request.method == 'POST':
        global g_prodcut_id_counter
        #Formdan verileri al
        name = request.form['name']
        price = float(request.form['price'])

        #Yeni ürünü oluştur
        new_prodcut = {
            'id':g_prodcut_id_counter,
            'name':name,
            'price':price
        }
        #Listeye ekle ve sayacı artır
        g_prodcut_id_counter += 1
        #Ekleme başarılı olursa ana sayfaya yönlendir
        return redirect(url_for('index.html'))
    # Get request is formu göster
    return render_template('add_product.html')

@app.route('/')

def index():
    #tüm ürünleri ana sayfada listele
    return render_template('index.html', prdocucts=prdocucts)


#CRUD - Update
@app.route('/edit/<int:product_id>', methods = ['GET','POST'])

def edit_product(product_id):
    #güncellenecek ürünü bul
    product = find_prodcut_by_id(product_id)
    if not product:
        return "Product not found", 404
    if request.method == 'POST':
        #Kullanıcı eğer forma değer girdiyse ürünü güncelle
        product['name'] = request.form['name']
        product['price'] = float(request.form['price'])
        return redirect(url_for('index'))

@app.route('/delete/<int:product_id>', methods = ['POST'])

def delete_product(product_id):
    product = find_prodcut_by_id(product_id)

    if product:
        prdocucts.remove(product)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)