# mfrc522

A python library to read/write RFID tags via the budget MFRC522 RFID module.

This code was published in relation to a [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/) and you can find out more about how to hook up your MFRC reader to a Raspberry Pi there.

## Installation

Until the package is on PyPi, clone this repository and run `python setup.py install` in the top level directory.

## Example Code

The following code will read a tag from the MFRC522

```python
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
```
