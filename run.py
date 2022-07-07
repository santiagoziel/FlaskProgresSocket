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

        socketio.emit("user acknowledgment", "inmediat")
        time.sleep(1)
        socketio.emit("user acknowledgment", "later")
        time.sleep(1)
        return "/progress"
    return render_template('index.html', form=form)

@app.route('/progress')
def ajax_index():
    return "10"

      # I want to load this in a progress bar

if __name__ == "__main__":
    app.run(debug=True)
