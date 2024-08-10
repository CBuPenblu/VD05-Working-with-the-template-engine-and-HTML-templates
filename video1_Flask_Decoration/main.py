from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "caption": "Movies about Harry",
        "link": "Watch the movie"
    }
    return render_template("index.html", **context)

@app.route("/shablon/")
def films2():
    context = {
        "caption": "Harry Potter",
                   "link": "Redirect to cinema"
    }
    return render_template("index.html", **context)

@app.route("/person/")
def characters():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()