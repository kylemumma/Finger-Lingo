import os
from label_image import fromFile
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
app = Flask(__name__)
'''
app.config['UPLOAD_FOLDER'] = 
photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos,))
'''
@app.route("/")
def hello():
	return render_template("index.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['photo']
		f.save("scripts/temp.jpg")
		return "<ul><li>"+ "</li><li>".join(fromFile("temp.jpg")) + "</li></ul>"
		#return redirect(url_for('hello'))
	  
'''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		#c.store()
		#flash("Photo save")
		#return redirect(url_for('show', id=rec.id))
	return render_template('upload.html')
'''	
'''@app.route('/photo/<id>')
def show(id):
	photo = Photo.load(id)
	if photo is None:
		abort(404)
	url = photos.url(photo.filename)
	return render_templates('show.html', url=url, photo=photo)'''

@app.route('/<path:path>')
def send_js(path):
    print (path)
    return send_from_directory('static/', path)
	
if __name__ == '__main__':
	app.run(debug=True)
	
