# 3-Tier-IoT-Architecture

Python, JSON, SQLite, HTML (basic)

Resful API: Flask for webpage


A 3 Tier Architecture IoT System

Sensor --> MQTT Broker ---> Database

Sensor generates fake data: Day, Windspeed, Energy Efficiency, Temperature

MQTT broker: using the mosquitto broker on local host, and using pub sub protocols, database application can subscribe to the sensor application to recieve data

Database: Store information that comes from the sensor


RESTFUL API:
Using flask, created endpoints for information in the database that can be accessed by a webpage. Data is retrieved in JSON format. 
