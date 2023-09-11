import asyncio
import websockets
import json
import random

# Initialize arm rotation and direction as global variables
arm_rotation = 0.1
direction = 1

async def arm_rotation_updater():
    global arm_rotation
    global direction

    while True:
        # Update arm rotation value
        arm_rotation += 0.1 * direction

        # Change direction when reaching 180 or 0.1
        if arm_rotation >= 180:
            direction = -1
        elif arm_rotation <= 0.1:
            direction = 1

        # Wait for 1 second before updating again
        await asyncio.sleep(1)

async def handler(websocket, path):
    while True:
        # Create a JSON object
        data = {
            "armMachine": [
                {
                    "temp": random.uniform(1.54, 3.5),
                    "vibration": random.uniform(1.53, 5.53),
                    "armRotation": round(arm_rotation, 2),  # Round to 2 decimal places
                    "Power": random.uniform(441.5, 555.5)
                }
            ],
            "machine_status": 0,
            "show_Demo_dye_change": 1
        }

        # Convert the JSON object to a string
        json_data = json.dumps(data)

        # Send the JSON string to the client
        await websocket.send(json_data)
        print(f"> {json_data}")

        # Wait for a short time before sending the next update
        await asyncio.sleep(1)

start_server = websockets.serve(handler, 0.0.0.0, 12345)

# Create a task for the arm rotation updater
rotation_updater_task = asyncio.get_event_loop().create_task(arm_rotation_updater())

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
