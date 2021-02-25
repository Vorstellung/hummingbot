import threading
from flask import Flask
from flask import request

app = Flask(__name__)
import asyncio
import time
import logging
log = logging.getLogger('werkzeug')
log.disabled = True
from hummingbot.core.utils.async_utils import safe_ensure_future

from hummingbot.client.hummingbot_application import HummingbotApplication

async def handle_command(command):
    hb = HummingbotApplication.main_application()
    try:
        await hb._handle_command(command)
    except:
        pass

    if command == "status":
        try:
            with open('data/status.txt', 'r') as f:
                return(f.read())
        except:
            return("Not started.")

    if command == "exit":
        try:
            with open('data/status.txt', 'w') as outfile:
                outfile.write("Stopped.")
        except:
            print("")

    return "OK"

@app.route('/')
def hello():
    command = request.args.get('command')
    asyncio.run(handle_command(command))
    return "OK"

def start_ah_interface():
    app.run(host='0.0.0.0',port=80,use_reloader=False)
    return "OK"

async def constant_status():
    while True:
        await handle_command("status")
        await asyncio.sleep(1)

def start_the_server():
    print("starting the flask system")
    threading.Thread(target=start_ah_interface, name="Flask Server").start()
    safe_ensure_future(constant_status())


