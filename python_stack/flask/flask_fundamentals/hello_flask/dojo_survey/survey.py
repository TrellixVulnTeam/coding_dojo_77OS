from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods = ["POST"])

def survey():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("show.html", name_on_template = name_from_form, 
    location_on_template = location_from_form, language_on_template = language_from_form, comment_on_template = comment_from_form)





if __name__ == "__main__":
    app.run(debug=True)