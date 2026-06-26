from flask import Flask, request, jsonify  # type: ignore[import]
from flask_restful import Resource  # type: ignore[import]
from flask_cors import CORS  # type: ignore[import]
import requests  # type: ignore[import]

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({"message": "Hello from GetRequester"})

