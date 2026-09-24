from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Python application is running successfully."

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/version")
def version():
    return {"application": "sample-python-app", "version": "1.0.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
