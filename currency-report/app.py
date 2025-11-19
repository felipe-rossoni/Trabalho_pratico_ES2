from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/quote', methods=['GET'])
def get_quote():
    curr_from = request.args.get('from','USD')
    curr_to  = request.args.get('to','BRL')

    response = {
        "from": curr_from,
        "to": curr_to,
        "price": 5.42,
        "timestamp": datetime.now().isoformat()
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100)
    