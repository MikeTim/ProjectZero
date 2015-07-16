#flask Site
from utils.fileio_v1 import read_file
from flask import Flask
module = Flask(__name__)
from flask import render_template


@module.route('/')
def root():
	return render_template("index.html", name = "fdfd")




if __name__ == "__main__":
	module.debug = True
	module.run()



