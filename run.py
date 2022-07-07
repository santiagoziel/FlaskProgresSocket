from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from flask_socketio import emit, SocketIO

from forms import deckUploadForm

import time, json

app = Flask(__name__)
app.config['SECRET_KEY'] = "fortheloveofgodchangethis"
app.config["UPLOAD_FOLDER"] = "txtFiles/"
socketio = SocketIO(app)


@socketio.on('connect')
def user_conecting():
    print("server acknowledgment")
    emit("user acknowledgment", "acknowledgment")

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = deckUploadForm()

    if form.validate_on_submit():
        #dta = json.loads(request.data.decode('utf-8'))
        #dta = request.form
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(app.config['UPLOAD_FOLDER'] + filename)
        #gen an id numner
        #here in reality in puting stuff into the db unde rthe id
        socketio.emit("updateBar", 25)
        time.sleep(1)
        socketio.emit("updateBar", 50)
        time.sleep(1)
        socketio.emit("updateBar", 75)
        time.sleep(1)
        socketio.emit("updateBar", 100)
        time.sleep(1)

        #plus the id number
        return "/progress"
    return render_template('index.html', form=form)

#this takes in a id number
@app.route('/progress')
def ajax_index():
    #get that id numbe from the fb, is contains all the info needed to pass to the template
    return render_template('progresBar.html')


if __name__ == "__main__":
    app.run(debug=True)
