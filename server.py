from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = "ids_logs.db"

def get_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, attack_type, source_ip, details FROM attack_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs

@app.route("/")
def index():
    logs = get_logs()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
