import os
import redis
import sys
from flask import Flask, request, render_template

app = Flask(__name__)
host = os.environ.get('REDIS_HOST')
port = os.environ.get('REDIS_PORT')
password = os.environ.get('REDIS_PW')
db = redis.Redis(
    host=host,
    port=port,
    password=password
)

def good_email(email):
    return True

@app.route('/')
def hello():
    # foo = db.get('foo')
    # if not foo:
    #     db.set('foo', 'bar')
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    print("REQUEST RCVD:", str(request.form))
    sys.stdout.flush()
    if good_email(request.form):
        return str(request.form['email'])
    else:
        return "Bad haxxor!"

if __name__ == '__main__':
    app.run()