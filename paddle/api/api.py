import time
from flask import Flask
import pickle
import os

app = Flask(__name__)

@app.route('/time')
def get_current_time():
	return {'time': time.time()}


@app.route('/count')
def get_count():
	try:
		with open('test.pickle', 'rb') as f:
			counter = pickle.load(f)
	except:
		counter = 0
	counter += 1
	with open('test.pickle', 'wb') as f:
		pickle.dump(counter, f)
	return {'count': counter}
