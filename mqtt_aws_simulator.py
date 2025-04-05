import paho.mqtt.client as paho
import os
import ssl
import time
import random
from datetime import datetime

awshost = "a1y2x3rx8mf6q0-ats.iot.us-east-2.amazonaws.com"
awsport = 8883
clientId = "DHT11_simulator"
topic = "update/environment/dht1"

caPath = "AmazonRootCA1 (1).pem"
certPath = "646f54239edf47ec7ba0e80cedd1a65d7c400a1032d116fdd0042687a9b4f653-certificate.pem.crt"
keyPath = "646f54239edf47ec7ba0e80cedd1a65d7c400a1032d116fdd0042687a9b4f653-private.pem.key"

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT with result code: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload))

mqttc = paho.Client(client_id=clientId)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.tls_set(ca_certs=caPath, certfile=certPath,
              keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_start()

while True:
    temperature = random.randint(20, 40)
    humidity = random.randint(30, 80)
    co2 = random.randint(400, 1500)
    timestamp = datetime.utcnow().isoformat()

    payload = '{{ "thingid": "dht1", "temperature": {}, "humidity": {}, "co2": {}, "datetime": "{}" }}'.format(
        temperature, humidity, co2, timestamp)

    print(f"Publishing: {payload}")
    mqttc.publish(topic, payload, qos=1)
    time.sleep(2)
