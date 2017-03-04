import os
import uuid
from flask import Flask, request, render_template \
                  , url_for, redirect, flash, make_response

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and request.form['username'] is not '':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            flash("Successfully logged in")
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', username)
            return response
        else:
            error = 'Incorrect username and password'

    return render_template('login.html', error=error)

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response

@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    app.debug = True
    app.run(host=host, port=port)
