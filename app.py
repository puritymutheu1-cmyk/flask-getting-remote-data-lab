from flask import Flask, jsonify
from flask_cors import CORS
from lib.GetRequester import GetRequester
import requests

app = Flask(__name__)
CORS(app)

EMPLOYEE_ENDPOINT = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

@app.route("/")
def index():
    return jsonify({"message": "Hello from GetRequester"})

@app.route("/employees")
def get_employees():
    try:
        requester = GetRequester(EMPLOYEE_ENDPOINT)
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

@app.route("/employees/raw")
def get_employees_raw():
    try:
        requester = GetRequester(EMPLOYEE_ENDPOINT)
        raw_data = requester.get_response_body()
        return raw_data, 200, {'Content-Type': 'application/json'}
    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to fetch raw data: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
