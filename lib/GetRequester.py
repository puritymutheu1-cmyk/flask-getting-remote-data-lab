from flask import Flask, request, jsonify  # type: ignore[import]
from flask_restful import Resource  # type: ignore[import]
from flask_cors import CORS  # type: ignore[import]
import requests  # type: ignore[import]

app = Flask(__name__)
CORS(app)

class GetRequester:
    EMPLOYEE_ENDPOINT = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

    def __init__(self, url: str):
        self.url = url

    def get_res_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = requests.get(self.url)
        return response.json()

@app.route("/")
def index():
    return jsonify({"message": "Hello from GetRequester"})

@app.route("/employees")
def get_employees():
    try:
        requester = GetRequester(GetRequester.EMPLOYEE_ENDPOINT)
        employees_data = requester.load_json()
        return jsonify({
            "status": "success",
            "data": employees_data
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to fetch employee data: {str(e)}"
        }), 500