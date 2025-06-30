from flask import Flask, render_template, request
from detector import detect_fake_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        news_input = request.form["news"]
        result = detect_fake_news(news_input)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
