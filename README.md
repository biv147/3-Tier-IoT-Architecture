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


How to run:

First go into your mosquitto directory, and run the command "mosquitto -p 1833"

There are 2 python files, app.py and sensor.py Once this repository is downloaded, go into the directory through any terminal of choice. To run the sensor, all you have to type is "python sensor.py. To run the flask server, you will have to type "flask run" (you will need another terminal for this)

Sensor.py will run without outputing anything, and the flask app will output what ever is recieved in the terminal. Also when the flask server is running, you can click the link it provides to go to the homepage, where there you can click on any link to see any json data
