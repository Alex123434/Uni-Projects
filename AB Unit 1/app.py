from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/HoodieMan")
def HoodieMan():
    return render_template("HoodieMan.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/SignUp")
def SignUp():
    return render_template("SignUp.html")

@app.route("/LogSignAcc")
def LogSignAcc():
    return render_template("LogSignAcc.html")

@app.route("/Man")
def Man():
    return render_template("Man.html")

@app.route("/TrousersMan")
def TrousersMan():
    return render_template("TrousersMan.html")

@app.route("/Woman")
def Woman():
    return render_template("Woman.html")

@app.route("/SneakersWoman")
def SneakersWoman():
    return render_template("SneakersWoman.html")

@app.route("/ShoppingCart")
def ShoppingCart():
    return render_template("ShoppingCart.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/TShirtsMan")
def TShirtsMan():
    return render_template("T-ShirtsMan.html")

@app.route("/SneakersMan")
def SneakersMan():
    return render_template("SneakersMan.html")

@app.route("/TrousersWoman")
def TrousersWoman():
    return render_template("TrousersWoman.html")

@app.route("/DressesWoman")
def DressesWoman():
    return render_template("DressesWoman.html")

@app.route("/HoodieWoman")
def HoodieWoman():
    return render_template("HoodieWoman.html")

if __name__ == "__main__":
    app.run(debug=True)