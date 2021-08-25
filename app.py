from flask import Flask, render_template, url_for, redirect, request, Response
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import cv2
from datetime import datetime

# Initialize an instance of a Flask Application
app = Flask(__name__, static_url_path='/static', instance_relative_config=True)
app.config['UPLOAD_FOLDER'] = '/uploads/'
app.config ['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:214497135@localhost/gvap"
db = SQLAlchemy(app)

class Video(db.Model):
    _ID = 0
    __tablename__= "Uploads"
    
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64))
    date_created = db.Column(db.DateTime)
    description = db.Column(db.Text)
    tags = db.Column(db.String(240))

    def __init__(self, name):  
        self.id = self._ID
        self.__class__._ID += 1
        self.file_name = name
        self.date_created = datetime.now()

# Create Database
db.create_all()

# Website endpoints 
@app.route('/')
def index():
    # Anything printed is automatically logged in the console
    print('New Visitor')
    
    # Get list of videos for user
    video_list = Video.query.filter().all()
    print("User has {} videos in their library".format(len(video_list)))
    return render_template('video_library.html', videos = video_list)

@app.route('/', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save("uploads/"+secure_filename(f.filename))
            msg = "{} was submitted successfully, Thank you!".format(f.filename)

            # Submit video entry to database
            new_video = Video(f.filename)
            print(new_video)
            db.session.add(new_video)
            db.session.commit()
            db.session.close()
            video_list = Video.query.filter().all()
            return render_template('video_library.html', type = "info", flash = msg, videos = video_list)
        except Exception as e:
            msg = "You must select a valid file for processing"
            print("Error: "+str(e))
            video_list = Video.query.filter().all()
            return render_template('video_library.html', type = "mild", flash = msg, videos = video_list)



@app.route('/annotate/<video_filename>')
def train(video_filename):
    # Get video by ID from database
    return render_template('video_annotations.html', video = video_filename)


@app.route('/query/<filename>')
def query(filename):
    f = open('trackers/center_net-center_track-person.txt', 'r')
    center_track = f.read()
    f.close()

    return render_template('video_query.html', video = filename, objects = center_track)


# Local Development environment
if __name__ == '__main__':
    # This is used when running locally
    # Gunicorn is used to run the application on Google App Engine
    # See entrypoint in app.yaml.
    app.run(host='localhost', port=8080, debug=True)








# Function that will break video into frames and send video to client frame by frame. 
# ( Yueting doesn't like this and would prefer that the tagging and video playback was done on the client side)
# def gen_frames():
#     # Dynamically load video by file_name passed in as parameter
#     cap = cv2.VideoCapture('./uploads/MOT17-11-SDP-raw.webm')
#     # cap = cv2.VideoCapture("./uploads/"+file_name)
#     while(True):
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                     b'Content-Type: images/jpeg\r\n\r\n'+frame+b'\r\n')
# @app.route('/video_feed')
# def video_feed():
#     # collect filename from parent page
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
