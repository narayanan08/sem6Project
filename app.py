from flask import url_for, render_template,Flask,request, redirect
import os

app=Flask(__name__)

app.config["UPLOAD_FOLDER"]="uploads"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def save_image():
    file=request.files['file']
    filename=file.filename
    file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
    return redirect(url_for("display_image",filename=filename))

@app.route("/display/<filename>")
def display_image(filename):
    return render_template("display.html",filename=filename)


if __name__=="__main__":
    app.run(debug=True)
