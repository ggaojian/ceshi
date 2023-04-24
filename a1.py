from flask import Flask
from datetime import datetime


app = Flask(__name__)
@app.route('/')
def index():
	now = datetime.now()
	
	return f"current time: {now}"
