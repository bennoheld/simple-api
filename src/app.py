import os
from flask import Flask

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return "", 200


@app.route("/ping", methods=["GET"])
def ping():
    return '🚀', 200


@app.route("/resource", methods=["GET"])
def get_resource():
    # Logic to get resource
    return "Resource retrieved successfully", 200


@app.route("/resource", methods=["POST"])
def create_resource():
    # Logic to create resource
    return "Resource created successfully", 201


@app.route("/resource", methods=["PUT"])
def update_resource():
    # Logic to update resource
    return "Resource updated successfully", 200


@app.route("/resource", methods=["DELETE"])
def delete_resource():
    # Logic to delete resource
    return "Resource deleted successfully", 204


if __name__ == "__main__":
    api_host = os.environ.get("API_HOST", "0.0.0.0")
    api_port = os.environ.get("API_PORT", "5003")
    app.run(host=api_host, port=api_port)
