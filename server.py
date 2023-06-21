from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("current_order.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, order=order, order_total=order_total)

@app.route("/cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("current_order.csv", cupcake=cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route("/cupcake_info/<name>")
def cupcake_info(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        return render_template("cupcake_info.html",cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route("/current_order")
def current_order():
    order = get_cupcakes("current_order.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("current_order.html", order=order, order_total=order_total)

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")
