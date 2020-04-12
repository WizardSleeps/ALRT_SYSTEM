import requests             # Used for HTTP requests
import json                 # Library for parsing/handling JSON Data
import time                 # Module for sleep-operation
import smtplib 
from boltiot import Bolt    # Imports Bolt form BoltIoT Module
import conf                 # Configuration File (conf.py)

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

def get_sensor_value_from_pin(pin):
    try:
        response = mybolt.digitalRead(pin)
        data = json.loads(response)
        sensor_value = int(data["value"])
        if sensor_value == 1:
            return sensor_value
        return 0
    except Exception as e:
        print("Something went wrong when returning the sensor values... try again!")
        print(e)
        return -999

def send_telegram_message(message):
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        reponse = requests.request(
            "POST",
            url,
            params=data
        )
        print("Telegram URL:")
        print(url)
        print("Telegram Resposne:")
        print(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("Error occurred when sending an alert message via Telegram... please check channel ID and Device ID!")
        print(e)
        return False

def send_mail(email, password, message):
    print("MESSAGE: " + message)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    print("Login Successful!")
    server.sendmail(email, "Project@Guiden.com", message) # Change email ID
    print("SENT")
    server.quit()

while True:
    sensor_value = get_sensor_value_from_pin("0")
    print("Current Sensor Value is: ", sensor_value)

    if sensor_value == -999:
        print("Something went wrong... check conf.py")
        time.sleep(10)
        continue

    if sensor_value == 1:
        print("Sensor value has exceeded threshold...")
        message = "Alert! Sensor has detected movement."
        telegram_status = send_telegram_message(message)
        print("Telegram Status:", telegram_status)

        email = "Project@Guiden.com"    # Enter Mail ID
        password = "GuidenProject"      # Enter Password for Mail ID
        send_mail(email, password, message)
        -
    time.sleep(10)