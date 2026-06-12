from flask import Flask, render_template
from analysis import get_results

app = Flask(__name__)

@app.route("/")
def home():
    data = get_results()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)