import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "demo/iot/sensors"


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

client.loop_forever()
