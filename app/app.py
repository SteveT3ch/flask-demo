from flask import Flask, request, render_template
import redis

app = Flask(__name__)
app.debug = True

@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return "User " + str(username)

@app.route('/post/<int:post_id')
def show_post(post_id):
    return "Post " + post_id

if __name__ == '__main__':
    app.run(host='0.0.0.0')
