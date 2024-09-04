from flask import Flask, request, jsonify
import json

app = Flask(__name__)

CODE_FILE = 'codes.json'

def load_codes():
    try:
        with open(CODE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/verify_code', methods=['POST'])
def verify_code():
    data = request.json
    code = data.get('code')
    user_id = data.get('user_id')
    codes = load_codes()

    if str(user_id) in codes and codes[str(user_id)] == code:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "fail"}), 400

if __name__ == '__main__':
    app.run()
