from flask import Flask, request, render_template \
                  , url_for, redirect, flash \
                  , make_response, session
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = '''
xRdLwljOJw+dP3b5cbDuPdoZH4DAXXUYmgAkePj\
TdiTE7f9aIpYKmp9u7beix5uzIUfNTDBo1WS3EMBk8Q'
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and request.form['username'] is not '':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            flash("Successfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and password'
            app.logger.warning("Incorrect username and password for user {}".format(username))
    return render_template('login.html', error=error)

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    app.debug = True

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setlevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=host, port=port)
