from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "poem": ["My heart leaps up when I behold",
                "A rainbow in the sky:",
                "So was it when my life began;",
                "So is it now I am a man;",
                "So be it when I shall grow old,",
                "Or let me die!",
                "The Child is father of the Man;",
                "And I could wish my days to be",
                "Bound each to each by natural piety."
                 ]

        # 1.2.3. "caption": "Movies about Harry",
        # 1. "user": "Igor"
        # 2. "number": 8
        # 3."list": ["Igors", "Kaspars", "Olga", "Silvija"]
    }
    return render_template("shablon.html", **context)

@app.route("/shablon")
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