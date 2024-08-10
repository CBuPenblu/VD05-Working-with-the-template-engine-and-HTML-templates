from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films2():
    context = {
        "link": "Redirect to cinema"
    }
    return render_template("index.html", **context)

@app.route("/person/")
def characters():
    context = {
        "link": "Redirect to cinema"
    }
    return render_template("main.html", **context)

if __name__ == "__main__":
    app.run()