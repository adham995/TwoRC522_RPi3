import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522(bus=0, device=0, pin_rst=15) #GPIO22

try:
        text = input('Enter Name: ') #set the name to RFID Card
        print("Place RF Tag/Card")
        reader.write(text) #write the name to RFID card
        print("Written") #print written when it get succesfull
finally:
        GPIO.cleanup() #clear data
