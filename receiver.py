import socketio
from config import *
import os
import time
from threading import Thread
from flask import Flask, render_template
import rospy
from std_msgs.msg import String
sio = socketio.Server(logger=True, async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)
app.config['SECRET_KEY'] = 'secret!'
thread = None    
rospy.init_node('receiver',anonymous=False)
pub = rospy.Publisher('receiver', String, queue_size=10)
@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')
	
@sio.on('message', namespace='/test')
def test_message(sid, message):
    data = message['data']
    rospy.loginfo(data)
    pub.publish(data)
#    sio.emit('response', {'data': message['data']}, namespace='/test')



@sio.on('connect', namespace='/test')
def test_connect(sid, environ):
    rospy.loginfo('Client connected')
    # try:
    #     p = subprocess.Popen(STREAM_START, stdout=subprocess.PIPE)
    #     connect()
    # except OSError as detail:
    #     print ("Could not execute " + STREAM_START[0] + " ", detail)
#    sio.emit('response', {'data': 'Server OK', 'count': 0}, room=sid,
#            namespace='/test')


@sio.on('disconnect', namespace='/test')
def test_disconnect(sid):
    # try:
    #     p = subprocess.Popen(STREAM_STOP, stdout=subprocess.PIPE)
    #     disconnect()
    # except OSError as detail:
    #     print ("Could not execute " + STREAM_STOP[0] + " ", detail)
    rospy.loginfo('Client disconnected')

# def connect():
#   i2ccom.start()
#   time.sleep(0.1)
#   i2ccom.sendMessage(CONNECT, -1)

# # Disconnect from rover
# def disconnect():
#   i2ccom.sendMessage(DISCONNECT, -1)
#   time.sleep(0.1)
#   i2ccom.stop()
# # Get current pid
# pid = os.getpid()


if __name__ == '__main__':
        app.run(threaded=True, host='0.0.0.0',port=5000)
    
