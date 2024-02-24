# from flask import Flask, render_template, Response
# from videocamera import VideoCamera  # Make sure this is the modified VideoCamera class

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')  # Assuming you have an index.html for video display

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template,Response
import cv2
from flask_socketio import SocketIO
import struct
import pickle

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    HOST = '192.168.252.241'
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')

    conn, addr = s.accept()

    data = b'' ### CHANGED
    payload_size = struct.calcsize("L") ### CHANGED

    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

        # Retrieve all data based on message size
        while len(data) < msg_size:
            data += conn.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Extract frame
        frame = pickle.loads(frame_data)    
        ## read the camera frame
        
        frame.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
