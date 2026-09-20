from flask import Flask, jsonify, render_template
import os
import socket

app = Flask(__name__)

APP_NAME = os.environ.get("APP_NAME", "app-2")
GREETING = os.environ.get("GREETING", "Hello from app-2")


@app.route("/")
def index():
    return render_template("index.html", name=APP_NAME, greeting=GREETING, host=socket.gethostname())


@app.route("/health")
def health():
    """Dedicated health endpoint so probes do not render the full page."""
    return jsonify(status="ok", app=APP_NAME), 200


@app.route("/ready")
def ready():
    return jsonify(status="ready", app=APP_NAME), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
