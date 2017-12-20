from lxml import html
import requests
import random

def bashquote( randnum ):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)
    quote = bashtree.xpath('//p[@class="qt"]/text()')
    quote_text = quotechequer(quote)
    print quote_text

def quotechequer ( quote_tbc ):
    if not quote_tbc:
        print "empty quote"
        bashquote(random.randint(7,963184))
    else:
        return quote_tbc

bashquote(random.randint(7,963184))
