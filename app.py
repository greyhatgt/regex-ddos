import os
import redis
from flask import Flask

app = Flask(__name__)
host = os.environ.get('REDIS_HOST')
port = os.environ.get('REDIS_PORT')
password = os.environ.get('REDIS_PW')
db = redis.Redis(
    host=host,
    port=port,
    password=password
)


@app.route('/')
def hello():
    foo = db.get('foo')
    if not foo:
        db.set('foo', 'bar')
    return "Hello, %s!" % str(foo)

if __name__ == '__main__':
    app.run()