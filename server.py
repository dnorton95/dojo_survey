from flask import Flask, render_template, session, redirect, url_for
from flask import request

app = Flask(__name__)
app.secret_key = 'password'  # Secret key for session management

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    print(request.form)
    session['fighter']= request.form['fighter']
    session['kameo']=request.form['kameo']
    session['villain']=request.form['villain']
    session['comment']=request.form['comment']
    session['fatality']=request.form['fatality']
    session['type']=request.form['type']
    return render_template('form.html',session=session)

@app.route("/form", methods=['POST'])
def form():
    return redirect(url_for('process'))

if __name__ == "__main__":
    app.run(debug=True)
