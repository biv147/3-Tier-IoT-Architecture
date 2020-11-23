import json
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template, jsonify
import sqlite3 as sql


#create the format for the table
TableSchema="""
drop table if exists Wind_Turbine_Data ;
create table Wind_Turbine_Data (
  DayNumber integer primary key autoincrement,
  WindSpeed text,
  EnergyEfficiency text,
  Temperature text
);
"""

#create/access the database
conn = sql.connect('database.db', check_same_thread=0)
curs = conn.cursor()

#create the tables
sql.complete_statement(TableSchema)
curs.executescript(TableSchema)

#flask name
app = Flask(__name__)

#callback function to retrieve message
def on_message(client, userdata, message):
    print("Data recieved: "+ str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("adding to database")
    Wind_Turbine_Data_Handler(message.payload)


#callback function to connect to the broker
def on_connect(client, userdata, flags, rc):
    print("connected ok!")
    client.subscribe("Data")

#handles the incoming data from the mqtt broker
def Wind_Turbine_Data_Handler(jsonData):
    # Parse Data
    json_Dict = json.loads(jsonData)
    Windspeed = json_Dict['Windspeed']
    EnergyEfficiency = json_Dict['EnergyEfficiency']
    Temperature = json_Dict['Temperature']

    # Push into DB Table
    sql = ("insert into Wind_Turbine_Data (Windspeed, EnergyEfficiency, Temperature) values (?,?,?)")
    data = [Windspeed, EnergyEfficiency, Temperature]
    curs.execute(sql, data)
    conn.commit()

#creating the client and connecting it
client = mqtt.Client()
client.on_message = on_message
print("connecting to broker")
client.connect("localhost", 1833, 60)  # connect to broker

#subsribing and getting the messages
client.on_connect = on_connect
client.on_message = on_message

#starting the loop
client.loop_start()


#endpoints
@app.route('/')
def hello_world():
    return render_template('home.html')


#endpoint 1
@app.route('/All')
def getAll():
    curs.execute("SELECT * FROM Wind_Turbine_Data")
    rv = curs.fetchall()
    data = []
    content = {}
    for result in rv:
        content = {'DayNumber': result[0], 'Windspeed': result[1], 'EnergyEfficiency': result[2], 'Temperature': result[3]}
        data.append(content)
    return jsonify(data)

#endpoint 2
@app.route('/Days')
def getDays():
    curs.execute("SELECT * FROM Wind_Turbine_Data")
    rv = curs.fetchall()
    data = []
    content = {}
    for result in rv:
        content = {'DayNumber': result[0]}
        data.append(content)
    return jsonify(data)

#endpoint 3
@app.route('/Speed_and_Efficiency')
def speedEff():
    curs.execute("SELECT * FROM Wind_Turbine_Data")
    rv = curs.fetchall()
    data = []
    content = {}
    for result in rv:
        content = {'Windspeed': result[1], 'EnergyEfficiency': result[2]}
        data.append(content)
    return jsonify(data)

#endpoint 4
@app.route('/TemperatureOverDays')
def list():
    curs.execute("SELECT * FROM Wind_Turbine_Data")
    rv = curs.fetchall()
    data = []
    content = {}
    for result in rv:
        content = {'DayNumber': result[0], 'Temperature': result[3]}
        data.append(content)
    return jsonify(data)

#running flask
if __name__ == '__main__':
    app.run()

