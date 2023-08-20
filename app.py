from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import sys
from flask_socketio import SocketIO


import re, uuid
# after each 2 digits, join elements of getnode().
# using regex expression
print ("The MAC address in expressed in formatted and less complex way : ", end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
#app = Flask(__name__)


from app import create_app, socketio

app = create_app(debug=True)

app.config['SECRET_KEY'] = 'meyubu!'
socketio1 = SocketIO(app)

@app.route('/io')
def index():
    return render_template('upload.html')

@socketio1.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio1.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio1.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio1.on('disconnect')
def test_disconnect():
    print('Client disconnected')


cur =os.getcwd()
app.config['UPLOAD_FOLDER']=cur +  "/uploads"
app.config['MAX_CONTENT_PATH']=1000
token="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"
@app.route('/upload')
def upload_file1():
   return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #os.chdir(cur + "/uploads/")
      f.save(secure_filename(f.filename))
      #os.close()
      return 'file uploaded successfully  <a href="/io">return </a>'



@app.route("/check/<name>")
def checkname(name):
    return  f"hello   {name}"

@app.route("/cached")
def cached():
    return render_template ("cache.html")

@app.route("/micmac")
def micmac():
    return  ':'.join(re.findall('..', '%012x' % uuid.getnode()))
if __name__ == '__main__':
   socketio.run(app)
