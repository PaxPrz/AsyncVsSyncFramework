from flask import Flask
from time import sleep, ctime

app = Flask("flaskapp")


@app.route("/sleeper")
def sleeper():
    request_arrival_time = ctime()
    sleep(10)
    request_delivery_time = ctime()
    return {
        "type": "sleeper",
        "arrival_time": request_arrival_time,
        "delivery_time": request_delivery_time,
    }


@app.route("/activer")
def activer():
    request_arrival_time = ctime()
    request_delivery_time = ctime()
    return {
        "type": "activer",
        "arrival_time": request_arrival_time,
        "delivery_time": request_delivery_time,
    }
