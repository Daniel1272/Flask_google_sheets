import os
import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Берём DATABASE_URL из Variables на Railway
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не задана!")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Создаём таблицу (если ещё нет)
cursor.execute("""
CREATE TABLE IF NOT EXISTS mytable (
    col1 TEXT,
    col2 TEXT
)
""")
conn.commit()

@app.route("/")
def index():
    return "Server is running!"

# Endpoint для обновления данных из Google Sheets
@app.route("/update", methods=["POST"])
def update():
    data = request.get_json().get("data")
    for row in data[1:]:  # пропускаем заголовок
        cursor.execute("INSERT INTO mytable(col1, col2) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
