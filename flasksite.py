from fileio_v1 import read_file
from flask import Flask

module = Flask(__name__)

@module.route('/')
def root():
	read_file("/static/index.html")
	return text



	


