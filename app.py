from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

#GET ONLY ROUTES
# @ signifies a decorator - way to wrap a function and modify it's behavior
@app.route("/")
def index():
    return 'Hello, Flask!!'

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route('/about')
def about():
    return '<h2>About</h2>'

@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef']
    return render_template("shopping.html", food=food)

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/product/<int:product_id>')
def product(product_id):
    return '<h2>Product ID is %s!</h2>' %product_id

#POST
@app.route("/login", methods=['GET', 'POST'])
def login():
    return "Method used: %s" % request.method

#Get data from the API
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if  __name__ == "__main__":
    app.run(debug=True)