from flask import Flask, jsonify
import json
  

with open('output.csv') as f:
    precip1 = f.read()

with open('output2.csv') as g: 
    stations_data=g.read()

with open('output3.csv') as h: 
    temperature_data=h.read()

with open('myfile.text') as i: 
    fifteen_days=i.read()


app = Flask(__name__)


@app.route("/api/v1.0/precipitation")
def climate():
    
    return jsonify(precip1)


@app.route("/api/v1.0/stations")
def climate2():

    return jsonify(stations_data)



@app.route("/api/v1.0/tobs")
def climate3():

    return jsonify(temperature_data)


@app.route("/api/v1.0/2017_07_09")
def climate4():

    return jsonify(fifteen_days)



@app.route("/")
def welcome():
    return ( f'api/v1.0/precipitation<br/>'
            f'api/v1.0/stations<br/>'
            f'api/v1.0/tobs<br/>'
            f'api/v1.0/2017_07_09'
    )


if __name__ == "__main__":
    app.run(debug=True)
