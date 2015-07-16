from flask import Flask,render_template
import markov_v2 as markov
import fileio_v1 as reader
from random import choice , random

tsm= Flask(__name__)

@tsm.route('/')
def home():
    return render_template('base.html',derp="Home",herp="Welcome!")
@tsm.route('/markov/')
@tsm.route('/markov/<source_text>')
def gen_markov(source_text="wonderland"):
    if source_text == "wonderland":
        chains = markov.generate_chains("wonderland.txt" )
        text = markov.generate_text( chains, 100 )
        header ="<!DOCTYPE html><html><head><title>Alice In Wonderland</title></head><h1>Markov Generator</h1><center><img src= 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Alice_par_John_Tenniel_30.png' height='200' width = '120'></br><button onclick='myFunction()'>Press me!</button><script> function myFunction(){  alert('WHY DID YOU PRESS ME!!!'); }</script><center></br><p>"
        footer ="</p></html>"
        final = "%s%s%s"%(header,text,footer)
        return final + render_template('base.html')
    elif source_text == "sawyer":
        chains = markov.generate_chains("sawyer.txt" )
        text = markov.generate_text( chains, 100 )
        header ="<!DOCTYPE html><html><head><title>The Adventures of Tom Sawyer</title></head><h1>Markov Generator</h1><img src= 'http://englishbookgeorgia.com/blogebg/wp-content/uploads/2014/06/Tom-Sawyer.jpg' height='200' width= '120'/></br><p>"
        footer ="</p></html>"
        final = "%s%s%s"%(header,text,footer)
        return final + render_template('base.html')
    elif source_text == "sherlock":
        chains = markov.generate_chains("sherlock.txt" )
        text = markov.generate_text( chains, 100 )
        header = "<!DOCTYPE html><html><head><title>The Adventures of Sherlock Holmes</title></head><h1>Markov Generator</h1><img src= 'http://www.internationalhero.co.uk/h/holmes_rathbone.jpg' height= '200' width = '120'/></br><p>"
        footer = "</p></html>"
        final = "%s%s%s"%(header,text,footer)
        return final + render_template('base.html')
    elif source_text == "war_of_the_worlds":
        chains = markov.generate_chains("war_of_the_worlds.txt" )
        text = markov.generate_text( chains, 100 )
        header = "<!DOCTYPE html><html><head><title>War of the Worlds</title></head><h1>Markov Generator</h1><img src='http://www.empireonline.com/images/image_index/300x250/3201.jpg' height='200' width='120'</br><p>"
        footer = "</p></html>"
        final = "%s%s%s"%(header,text,footer)
        return final + render_template('base.html')
    else:
        return("Book is not available at the moment")
@tsm.route('/L337')
def leet():
    return ('y0u 4r3 4n 3l173 h4ck3r.') + render_template('base.html')
@tsm.route('/TSM')
def TSM():
    return('You found the hidden page on this site. Congrats! Now you get a cookie.') + render_template('base.html')
if __name__ == '__main__':
    tsm.debug=True
    tsm.run()
