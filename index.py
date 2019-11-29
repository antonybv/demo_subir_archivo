from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "D:\\PHYTON\\Demo\\static\\images\\uploads"
@app.route("/upload-image", methods=["GET","POST"])
def uploadImages():
    if request.method == 'POST':
        print("-")
        print(request.files['file'])
        print("-")
        """ if request.files: 
            image = request.files[0]
            image.filename = "Hola mundo 222.png"
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
    
            return redirect(request.url) """
    return render_template("upload.html")


if __name__ == '__main__':
    app.run(debug=True)

    
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return "About"
