import threading
from flask import Flask
app = Flask(__name__)
import asyncio
loop = asyncio.get_event_loop()

import logging
log = logging.getLogger('werkzeug')
log.disabled = True

from hummingbot.client.hummingbot_application import HummingbotApplication

async def handle_command(command):
    hb = HummingbotApplication.main_application()
    await hb._handle_command(command)

@app.route('/')
def hello():
    asyncio.run(handle_command("order_book"))
    return "OK"

def start_ah_interface():
    app.run(host='0.0.0.0',port=80,use_reloader=False)
     return "OK"

def start_the_server():
    print("starting the flask system")
    threading.Thread(target=start_ah_interface, name="Flask Server").start()
    
    