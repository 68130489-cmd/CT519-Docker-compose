from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        value = request.form.get("value")

        response = requests.post(API_URL, json={
            "value": float(value)
        })

        if response.status_code == 200:
            result = response.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
