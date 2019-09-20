from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import os, sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# if 'SUMO_HOME' in os.environ:
#     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
#     sys.path.append(tools)
# else:
#     sys.exit("please declare environment variable 'SUMO_HOME'")
#
# sumoBinary = os.path.join(os.environ['SUMO_HOME'], 'bin/sumo-gui')
# sumoCmd = [sumoBinary, "-c", "GenericWorld.sumocfg", "--start"]

import traci

@app.before_first_request
def activate():
    # traci.start(sumoCmd)
    # step = 0
    # while step < 1000:
    #     traci.simulationStep()
    #     # for veh_id in traci.vehicle.getIDList():
    #     #         print traci.vehicle.getSpeed(veh_id)
    #     step += 1

    # print traci.lane.getEdgeID(':1126_1_0')
    # traci.close()
    pass

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(message):
    # send(traci.lane.getEdgeID(':1126_1_0'))
    print("this is message")
    send("got message")

@socketio.on('my event')
def handle_message(msg):
    print(msg)
    send("got message")

@app.route('/')
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    app.debug = True
    socketio.run(app, port=8848)
