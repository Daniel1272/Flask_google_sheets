from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    values = data.get("values", [])

    print("Получены данные из таблицы:")
    for row in values:
        print(row)

    # 👇 здесь твоя логика работы с данными
    # process(values)

    return jsonify({"status": "ok", "rows": len(values)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)



