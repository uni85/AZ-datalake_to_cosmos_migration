from flask import Flask, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route('/api/bikes', methods=['GET'])
def get_bike_data():
    # This simulates a real-time response from a bike-sharing provider
    data = {
        "id": str(uuid.uuid4()), # Unique ID for the record
        "station_id": "001",
        "city": "Paris",
        "available_bikes": 9,
        "total_docks": 20,
        "timestamp": datetime.utcnow().isoformat()
    }
    return jsonify(data)

if __name__ == '__main__':
    # Runs on all interfaces so the ADF can reach the VM via its Public IP
    app.run(host='0.0.0.0', port=5000)