import paho.mqtt.client as mqtt
import serial
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
# Define callback functions for MQTT events
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to the topic when connected
    client.subscribe("check")

def on_message(client, userdata, msg):
    
    if msg.payload == b'alldown':
        print("all down")
        write_read("1")
        


    if msg.payload == b'mf':
        print("middle finger")
        write_read("2")

    if msg.payload == b'if':
        print("index finger")
        write_read("3")

    if msg.payload == b'v':
        print("victory")
        write_read("4")

    if msg.payload == b't':
        print("thumb")
        write_read("5")


    if msg.payload == b'90':
        print("ninety")
        write_read("6")


    if msg.payload == b'l':
        print("looser")
        write_read("7")


    if msg.payload == b'allup':
        print("all up")
        write_read("8")
    
    
    

# Connect to the MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

# Start the MQTT client loop
client.loop_start()
print("started")

# Publish a message to the topic
#client.publish("mytopic", "Hello, MQTT!")

# Wait for messages to be received
while True:
    pass

# Stop the MQTT client loop
#client.loop_stop()
