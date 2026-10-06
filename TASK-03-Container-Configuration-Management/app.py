import os
from flask import Flask, jsonify

app = Flask(__name__)

ENV_MODE = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
CONFIG_PATH = "/app/config/settings.json"

@app.route('/config')
def get_config():
    file_content = "File not found"
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            file_content = f.read()
            
    return jsonify({
        "environment": ENV_MODE,
        "log_level": LOG_LEVEL,
        "mounted_config": file_content
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)