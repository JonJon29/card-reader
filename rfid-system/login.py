#!/bin/python3
import json
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

from datetime import datetime

data = []
try:
    with open('./data_base.json', 'r') as f:
        data = json.load(f)

except IOError:
    with open('./data_base.json', 'w+') as f:
        f.write("{}")

try:
    while True:
        id, text = reader.read()
        today = datetime.today().strftime("%d/%m/%Y")
        current_time = datetime.now().strftime("%H:%M:%S")

        #add date to json
        if(not today in data.keys()):
          data[str(today)] = {}

        #add name to json
        with open('./users.json', 'r') as g:
          user_list = json.load(g)
        user = ""
        if str(id) in user_list:
            user = user_list[str(id)]
        else:
            print("ID unknown, please register your card first")
            sleep(1)
            continue 
        if(not str(user) in data[str(today)]):
          data[str(today)][str(user)] = {}

        #add date and id
        if("time-in" in data[str(today)][str(user)]):
          if(not "time-out" in data[str(today)][str(user)]):
            data[str(today)][str(user)]["time-out"] = current_time
            print("logged out")
        else:
          data[str(today)][str(user)]["id"] = str(id)
          data[str(today)][str(user)]["time-in"] = current_time
          print("logged in")


        with open('data_base.json', 'w') as outfile:
          outfile.write(json.dumps(data, indent=4, sort_keys=True))
        sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
