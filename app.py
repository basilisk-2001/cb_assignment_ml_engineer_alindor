from flask import Flask, flash, request, redirect, url_for
import os
from testlangchain import *
from speech_to_text import *
#from audiodecode import *
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file :#and allowed_file(file.filename)
            filename = file.filename#secure_filename(
            outputFromSTTVariable = speech_to_text_function(file)
            outOpenai = outputFromSTTVariable
            outOpenai = outputFromOpenai(str(outOpenai))
            return {"gpt-response":json.loads(outOpenai)}
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
# import dotenv
# dotenv.load_dotenv('./.env')
# print(os.environ['SECRET_KEY'])

#run -> flask --app app run
#Authorization: Token <YOUR_SECRET>
if __name__ == '__main__':
    app.run(debug=True)