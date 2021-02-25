import threading
from flask import Flask
from flask import request

app = Flask(__name__)
import asyncio

import logging
log = logging.getLogger('werkzeug')
log.disabled = True

from hummingbot.client.hummingbot_application import HummingbotApplication

async def handle_command(command):
    hb = HummingbotApplication.main_application()
    try:
        await hb._handle_command(command)
    except:
        print("Caught it.")

    return "OK"

@app.route('/')
def hello():
    command = request.args.get('command')
    asyncio.run(handle_command(command))
    return "OK"

def start_ah_interface():
    app.run(host='0.0.0.0',port=80,use_reloader=False)
    return "OK"

def start_the_server():
    print("starting the flask system")
    threading.Thread(target=start_ah_interface, name="Flask Server").start()
    
    