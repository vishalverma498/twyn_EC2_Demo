import asyncio
import json
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for development purposes

# Initialize arm rotation and direction as global variables
arm_rotation = 0.1
direction = 1

graph30_data = []  # Initialize an empty list to store 30 data points

@app.route('/arm_data', methods=['GET'])
def get_arm_data():
    global arm_rotation
    data = {
        "armMachine": [
            {
                "temp": random.uniform(1.54, 3.5),
                "vibration": random.uniform(1.53, 5.53),
                "armRotation": round(arm_rotation, 2),
                "Power": random.uniform(441.5, 555.5)
            }
        ],
        "machine_status": 0,
        "show_Demo_dye_change": 1
    }
    return jsonify(data)

@app.route('/graph30', methods=['GET'])
def get_graph30_data():
    global graph30_data
    while len(graph30_data) < 30:
        new_data_point = {
            "Health": round(random.uniform(0, 100), 2),
            "OEE": round(random.uniform(0, 100), 2),
            "Temperature": round(random.uniform(0, 500), 2),
            "Vibration": round(random.uniform(0, 100), 2),
            "Pressure": round(random.uniform(0, 500), 2),
            "Power": round(random.uniform(0, 150), 2),
            "Production": round(random.uniform(0, 500), 2)
        }
        graph30_data.append(new_data_point)

    data = json.dumps(graph30_data)
    graph30_data = []  # Clear the list for the next 30 data points
    return data

@app.route('/graph', methods=['GET'])
def get_graph_data():
    data = {
        "Health": round(random.uniform(0, 100), 2),
        "OEE": round(random.uniform(0, 100), 2),
        "Temperature": round(random.uniform(0, 500), 2),
        "Vibration": round(random.uniform(0, 100), 2),
        "Pressure": round(random.uniform(0, 500), 2),
        "Power": round(random.uniform(0, 150), 2),
        "Production": round(random.uniform(0, 500), 2)
    }
    return jsonify(data)

@app.route('/motor', methods=['GET'])
def get_motor_data():
    data = {
        "Motor1T": round(random.uniform(0, 500), 2),
        "Motor2T": round(random.uniform(0, 500), 2),
        "Motor3T": round(random.uniform(0, 500), 2),
        "Motor4T": round(random.uniform(0, 500), 2),
        "Motor1V": round(random.uniform(0, 100), 2),
        "Motor2V": round(random.uniform(0, 100), 2),
        "Motor3V": round(random.uniform(0, 100), 2),
        "Motor4V": round(random.uniform(0, 100), 2)
    }
    return jsonify(data)

@app.route('/bolster', methods=['GET'])
def get_bolster_data():
    data = {
        "bolster1V": round(random.uniform(0, 200), 2),
        "bolster2V": round(random.uniform(0, 200), 2),
        "bolster3V": round(random.uniform(0, 200), 2),
        "bolster4V": round(random.uniform(0, 200), 2)
    }
    return jsonify(data)

@app.route('/dye', methods=['GET'])
def get_dye_data():
    data = {
        "Dye1T": round(random.uniform(0, 300), 2),
        "Dye2T": round(random.uniform(0, 300), 2),
        "Dye3T": round(random.uniform(0, 300), 2),
        "Dye4T": round(random.uniform(0, 300), 2)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='13.233.35.226', port=12345, threaded=True)
