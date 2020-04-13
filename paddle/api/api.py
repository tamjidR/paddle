import time
from flask import Flask

app = Flask(__name__)

@app.rout('/time')
def get_current_time():
	return {'time': time.time()}