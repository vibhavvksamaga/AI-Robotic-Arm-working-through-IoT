import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with a result code :" + str(rc))
    client.subscribe("check")

def on_message(client, userdata, msg):
    if msg.payload == "alldown":
        print("all down")


    if msg.payload == "mf":
        print("middle finger")

    if msg.payload == "if":
        print("index finger")

    if msg.payload == "v":
        print("v shape")

    if msg.payload == "t":
        print("thumb")


    if msg.payload == "90":
        print("90 Degree")


    if msg.payload == "l":
        print("L shape")


    if msg.payload == "allup":
        print("all up")
    





def func1():
    print("all down")
    publish.single("check", "alldown", hostname="broker.hivemq.com")
    print("ok")


def func2():
    print("middle finger")
    publish.single("check", "mf", hostname="broker.hivemq.com")


def func3():
    print("index finger")
    publish.single("check", "if", hostname="broker.hivemq.com")


def func4():
    print("Victory")
    publish.single("check", "v", hostname="broker.hivemq.com")


def func5():
    print("thumb")
    publish.single("check", "t", hostname="broker.hivemq.com")


def func6():
    print("ninty degree")
    publish.single("check", "90", hostname="broker.hivemq.com")


def func7():
    print("Loser")
    publish.single("check", "l", hostname="broker.hivemq.com")


def func8():
    print("All up")
    publish.single("check", "allup", hostname="broker.hivemq.com")


while True:
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883, 60)
    
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                func1()
                    
            if fingerup == [0, 0, 1, 0, 0]:
                func2()
                    
            if fingerup == [0, 1, 0, 0, 0]:
                func3()
                    
                    
            if fingerup == [0, 1, 1, 0, 0]:
                func4()
                    
            if fingerup == [1, 0, 0, 0, 0]:
                func5()
                    
            if fingerup == [1, 0, 1, 0, 0]:
                func6()
                    
                    
            if fingerup == [1, 1, 0, 0, 0]:
                func7()
                    
                    
            if fingerup == [1, 1, 1, 0, 0]:
                func8()


    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        time.sleep(0.3)
video.release()
cv2.destroyAllWindows()
