from time import sleep
import sys
from mfrc522 import SimpleMFRC522
from threading import Thread

device_0_reader = SimpleMFRC522(bus=0, device=0, pin_rst=15) #GPIO22
device_1_reader = SimpleMFRC522(bus=0, device=1, pin_rst=13) #GPIO27

def readFrom_reader_1():
    try:
        while True:
            print("Hold a tag near the reader")
            id = device_0_reader.read_id()
            print("ID-1 : ", id)
            sleep(0.5)
    finally:
        GPIO.cleanup()
        


def readFrom_reader_2():
    try:
        while True:
            print("Hold a tag near the reader")
            id = device_1_reader.read_id()
            print("ID-2 : ", id)
            sleep(0.5)
    finally:
        GPIO.cleanup()

t1 = Thread(target=readFrom_reader_1)
t2 = Thread(target=readFrom_reader_2)

# start the threads
t1.start()
t2.start()