import datetime
import os
import re
import redis
import time
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
    if not email:
        return False
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", str(email)):
        return True
    else:
        return False

@app.route('/')
def hello():
    # foo = db.get('foo')
    # if not foo:
    #     db.set('foo', 'bar')
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    email = request.form.get('email', None)
    if good_email(email):
        db.set('goodemail:' + str(email), date)
        return str(email)
    else:
        db.set('bademail:' + str(email), date)
        return "Bad haxxor!"

if __name__ == '__main__':
    app.run()