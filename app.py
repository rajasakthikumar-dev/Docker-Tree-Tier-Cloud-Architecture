from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend is Running!"

@app.route("/api")
def api():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="appuser",
            password=os.environ["DB_PASSWORD"],
            database="appdb"
        )

        connection.close()

        return "SUCCESS: Backend connected to MySQL Database!"

    except Exception as e:
        return f"Database connection failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)