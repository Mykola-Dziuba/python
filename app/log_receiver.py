# log_receiver.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pydantic import BaseModel
from typing import List

app = Flask(__name__)
CORS(app)

# Список для хранения логов
logs_storage = []


class LogEntry(BaseModel):
    pod_name: str
    log: str


@app.route("/logs/", methods=["POST"])
def receive_logs():
    log_entry = request.json
    logs_storage.append(log_entry)  # Сохраняем логи в список
    return jsonify({"message": "Log received"}), 200


@app.route("/logs/", methods=["GET"])
def get_logs():
    return jsonify(logs_storage), 200


@app.route("/")
def index():
    return render_template("index.html")  # Рендеринг главной страницы


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Запуск Flask приложения
