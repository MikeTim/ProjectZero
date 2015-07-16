from random import random,randint
import Name as fill

#words =fill.get_csv_list('wordlist.csv')
articles=["The","A","One","No"]
#adjectives=["blue","red","big","yellow","tall","small","smelly"]
#nouns=["desk","car","girl","boy","chair","laptop"]
#verbs=["eats","sleeps","works", "jumps","swims","plays"]
#DO=["soccer","food","bed","pool"]
#adverbs=["quickly","slowly","rapidly"]
#adjectives = words[2]
#nouns = words[0]
#verbs = words[1]
#DO = words[0]
#adverbs = words[3]
words= fill.get_csv_dict('wordlist.csv')
nouns=words['nouns']
verbs=words['verbs']
adjectives=words['adjectives']
adverbs=words['adverbs']
DO=words['nouns']
def OneOf(k):
    return k[int(random()*len(k))]


def pick1(k):
    ran= randint(0,1)
    if ran == 0:
        return ''
    if ran == 1:
        return OneOf(k)
def pick2(k):
    rant= random()
    if rant > .5:
        return ''
    else:
        return OneOf(k)+ ' ' + pick2(k)

        
def nounPhrase():
    return pick1(articles)+' '+ pick2(adjectives) + ' ' + OneOf(nouns) + ' '
def verbPhrase():
    return OneOf(verbs)+ ' ' + pick1(DO) + ' '+ pick1(adverbs)+'.'


def sengen():
    return nounPhrase() + verbPhrase()
