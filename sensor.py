import json
import paho.mqtt.client as mqtt
import time
import random


def main():
    #creating the client and connecting the client
    client = mqtt.Client()
    client.connect("localhost", 1833, 60)

    #units for the info
    a = " km/h"
    b = " %"
    c = " C"

    i = 1
    while i < 1000:
        #generating the data, x = windspeed, y = energy efficiency, z = temperature
        z = random.randint(5, 30)
        x = random.randint(0, 30)

        #getting energy efficiency depending on the windspeed
        y = 0
        if (x <= 5):
            y = 25
        elif (x > 5 and x <= 10):
            y = 50
        elif (x > 11 and x <= 13):
            y = 80
        elif (x > 13 and x < 17):
            y = 100
        elif (x > 18 and x <= 20):
            y = 80
        elif (x > 20 and x <= 25):
            y = 50
        elif (x > 25 and x <= 30):
            y = 20

        #combining data with units
        wind = str(x) + ' km/h'
        energy = str(y) + ' %'
        temp = str(z) + ' C'

        #combining all data into one variable
        Data = {}
        Data['Windspeed'] = wind
        Data['EnergyEfficiency'] = energy
        Data['Temperature'] = temp
        Data_Json = json.dumps(Data)

        #publishing the data
        client.publish("Data", Data_Json)
        time.sleep(1)

        i += 1

if __name__ == '__main__':
    main()