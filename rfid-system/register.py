#!/bin/python
import json
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

users = []
try:
    with open('./users.json', 'r') as f:
        users = json.load(f)

except IOError:
    with open('./users.json', 'w+') as f:
        f.write("{}")

try:
    while True:
        id, text = reader.read()
        name = input("Register new user: ")
        with open('./users.json', 'r') as gf:
            data = json.load(gf)
        data[str(id)] = str(name)
        
        with open('./users.json', 'w') as out:
            out.write(json.dumps(data, indent=4, sort_keys=True))



except KeyboardInterrupt:
    GPIO.cleanup()
    raise
