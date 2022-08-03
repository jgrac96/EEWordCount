# James Grace
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "8d6269c6211afe326c16a2aabe72eea0b55ac5da46be1cd5"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        no_words = len(str(request.form["content"]).split())
        print(no_words)
        return redirect(url_for("index"))
    return render_template("index.html")

app.run(debug=True)
