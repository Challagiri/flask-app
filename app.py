from flask import Flask

app = Flask(__name__)

x = 123


@app.route("/")
def home():
    return "Hello, Kubernetes!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
