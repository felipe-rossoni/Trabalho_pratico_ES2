from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/history', methods=['GET'])
def get_history():
    curr_from = request.args.get('from', 'USD')
    curr_to = request.args.get('to', 'BRL')
    
    now = datetime.now()
    
    # Mock de histórico (array simples)
    history_data = [
        {
            "timestamp": (now - timedelta(days=1)).isoformat(),
            "price": 5.35
        },
        {
            "timestamp": now.isoformat(),
            "price": 5.42
        }
    ]
    
    response = {
        "from": curr_from,
        "to": curr_to,
        "values": history_data
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    # Roda na porta 8101
    app.run(host='0.0.0.0', port=8101)