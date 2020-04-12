# ALRT_SYSTEM
Alert System using BoltIoT and PIR

# Building the circuit
(1.) Connect three female pins to the PIR Motion Sensor
(2.) Connect the positive (+) pin of the sensor to the 5V Bolt-Module
(3.) Connect the ground (-) pin of the sensor to the GND pins of the Bolt-Module
(4.) Connect the output pin of the sensor to the digital 0 (D0) on the Bolt Module

# Requirements
(a.) BoltIoT WiFi-Module
(b.) PIR Sensor (https://www.miniinthebox.com/en/p/pyroelectric-infrared-pir-motion-sensor-detector-module_p903342.html?currency=USD&litb_from=bing_shopping&country_code=us&utm_source=bingshopping&utm_medium=cpc&utm_campaign=bingshopping&msclkid=28017ee834471dc48949207ad952f96e)

# Module Install
sudo pip install boltiot

# Overview
I decided to create an Alert-System, the project will use a PIR (Passive Infared)
Motion Sensor, which will use detectors. Each of the sensor circuits will have an advanced
system that will use the PIR sensor to detect motion, and will notify you via Telegram, or Email.

# Mail System
SMTP Library in python

# How it works
(1.) Place the sensor output value to low (1-96pv)
a. When sensor goes off, it will change the sensor output value to a higher level.

# How does a PIR work
Normally a PIR output value is 0, when a PIR sensor detects motion the output value will be higher
such as 1. Although, when the sensor output becomes 1 (using the Python Code), it will send a Email
through SMTP Library and also Telegram (API).
