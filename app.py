# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import additional libraries below
import numpy as np
import cv2

app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # write the read and write function on image below 
    read_file=make_grayscale(file.read())
    with open(os.path.join('static/',filename),'wb') as f:
    	f.write(read_file)



        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


# Write the make_grayscale() function below
def make_grayscale(input_image):
	image_array=np.fromstring(input_image,dtype="uint8")
	print("Image as an array:",image_array)

	decoded_array=cv2.imdecode(image_array,cv2.IMREAD_UNCHANGED())
	print("Image after being decoded:",decoded_array)

	converted_image=cv2.cvtColor(decoded_array,cv2.COLOR_RGB2GRAY)
	status,output_image-cv2.imencode(".PNG",converted_image)

	print("Status of image:",status)
	return output_image








# make_grayscale() function ends above

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


