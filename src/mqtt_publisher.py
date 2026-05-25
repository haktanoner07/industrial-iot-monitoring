import json
import random
import time

while True:
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)

    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "status": 1
    }

    print(json.dumps(payload))

    time.sleep(2)
