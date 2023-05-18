from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "potatoes"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html")


if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)