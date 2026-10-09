import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health')
def health():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        conn.close()
        return jsonify({"status": "UP", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)