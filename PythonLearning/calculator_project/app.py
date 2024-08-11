from flask import Flask, render_template

# setting up the server
app = Flask(__name__)

@app.route ('/home')
def home():
    return "Hello, Word!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/calculate')
def calculate():
    return render_template("index.html")
@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    result = a+b
    return render_template("index.html", result=result)

@app.route('/sub/<int:a>/<int:b>')
def sub(a,b):
    result = a-b
    return render_template("index.html", result=result)

@app.route('/multi/<int:a>/<int:b>')
def multi(a,b):
    result = a*b
    return render_template("index.html", result=result)

@app.route('/div/<int:a>/<int:b>')
def div(a,b):
    result = a/b
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)