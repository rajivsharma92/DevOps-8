###Ecommerce piece

###create a list of Dictionary: Products

###create a get api for getting product information : Allproducts, byProductID

from flask import Flask, jsonify, request

app = Flask(__name__)

products = [ {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10}, 
                {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 20}, 
                {"id": 3, "name": "Tablet", "price": 299.99, "stock": 15}, ]

@app.route('/')
def home():
    return jsonify("Welcome to my nakli ecom website")

@app.route('/getAllproducts', methods = ['GET'])

def getAllProducts():
    
   return jsonify(products)
# Added <int:product>
@app.route('/products/<product_id>', methods=['GET']) 
def get_product_by_id(product_id):
    for p in products:
        if p["id"] == int(product_id):
            return jsonify(p)
    else:
        return jsonify({"error": "Product not found"}), 404 

@app.route('/product', methods=['GET'])
def get_product_ids_and_names():
    # Extracting only the id and name
    id_name_pairs = [{"id": product["id"], "name": product["name"]} for product in products]
    return jsonify(id_name_pairs)

@app.route('/addProduct', methods= ['POST'])

def add_product():
    product = request.json
    
    for p in products:
        if p['id'] == product['id']:
            return jsonify({"error": "Product with this ID already exists"}), 400
    
    products.append(product)
    return jsonify(product), 201
    
if __name__ == '__main__':
    app.run(debug=True)