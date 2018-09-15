from flask import Flask

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify it's behavior
@app.route("/")
def index():
    return 'Hello, Flask!!'

@app.route('/about')
def about():
    return '<h2>About</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s!" %username

@app.route('/product/<int:product_id>')
def product(product_id):
    return '<h2>Product ID is %s!</h2>' %product_id


if  __name__ == "__main__":
    app.run(debug=True)