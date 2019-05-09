# we need a microservice which has the client within it and the client talks to the server
# so this flask app is a simple microservice which is conneacted to the client
from flask import Flask, render_template, redirect, url_for, flash, request
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload
from grpc_client import remote_procedure_call
import  os
import json

app = Flask(__name__)
app.secret_key='uoifuxaiuyoiaayxyaoinyafoxpaiffpifyaxfanx'
os.environ['CLOUDINARY_URL'] = 'cloudinary://663314969728525:yENrtmlHycsoRVV9PC_1jl5sDZw@sharan'
print(os.environ)

@app.route('/',methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html', data={})
    else:
        # get the images from the form
        files = request.files.getlist("image[]")
        image_urls = []
        if len(files) != 2:
            flash("Please upload 2 files")
            return redirect(url_for('home'))
        for file in files:
            if file.filename == "":
                flash("Please select file")
                return redirect(url_for('home'))
            else:
                #upload each of the image to cloudinary
                try:
                    upload_result = upload(file)
                    # fetch the urls of the image uploaded to cloudinary
                    image_url, options = cloudinary_url(upload_result['public_id'], format="jpg")
                    image_urls.append(image_url)
                except Exception as E:
                    flash(str(E))
                    return redirect(url_for('home'))
        # call the grcp here
        # pass the images to grpc client so that it can make rpc to server
        response_data = remote_procedure_call(image_urls)
        return render_template('home.html', data=response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
