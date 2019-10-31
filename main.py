from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") #Esta é a parte que indica em qual URL esse manipulador pode ser acessado. Atualmente ele é definido como a raiz do site: /. Isso significa que sempre que formos para http://127.0.0.1:5000/, essa função será chamada e retornará o index.htmlmodelo.
def index():

    return render_template("index.html")


@app.route("/about.html")
def about():
    render_template("about.html")

if __name__ == '__main__':
    app.run()