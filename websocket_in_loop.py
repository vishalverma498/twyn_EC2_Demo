import asyncio
import websockets
import json
import datetime
import random

async def handler(websocket, path):

    while True:
        # create a JSON object
        data = {
            "ObjctId": "Conveyer ",
            "Health": random.uniform(13.5, 53.5),
            "OEE": random.uniform(122.5, 522.5),
            "Temperature": [
                random.uniform(1.54, 3.5), random.uniform(1.53, 5.53),random.uniform(1.5, 5.5)
            ],
            "Vibration": random.uniform(121.5, 215.5),
            "Pressure": random.uniform(221.5, 335.5),
            "Power": random.uniform(441.5, 555.5),
            "Production": random.uniform(661.5, 775.5)
        }
        # "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # "message": "Hello, Client!"

        # convert the JSON object to a string
        json_data = json.dumps(data)
        # send the JSON string to the client
        await websocket.send(json_data)
        print(f"> {json_data}")
        # wait for 1 second
        await asyncio.sleep(1)

start_server = websockets.serve(handler, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
