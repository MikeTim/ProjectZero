#flask Site
from utils.fileio_v1 import read_file
from flask import Flask
module = Flask(__name__)
from flask import render_template


@module.route('/')
def root():
	return render_template("index.html", name = "Project Zero - C-Stuy", title = "Project Zero", Stuff = "Landjaeger picanha tenderloin prosciutto corned beef. Salami ham hock flank jerky, picanha pancetta turducken cow strip steak fatback chicken pork loin capicola. Ribeye tenderloin corned beef hamburger brisket ball tip. Spare ribs frankfurter hamburger jowl pastrami pancetta pork loin chuck kevin short loin pork bresaola beef ribs boudin meatball.")

@module.route('/')


if __name__ == "__main__":
	module.debug = True
	module.run()



