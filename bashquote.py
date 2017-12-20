from lxml import html
import requests
import random

def bashquote( randnum ):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)
    quote = bashtree.xpath('//p[@class="qt"]/text()')
    quote_text = quotechequer(quote)
    print "quote_text is of type: " + str(type(quote_text))
    yield quote_text

def quotechequer ( quote_tbc ):
    if not quote_tbc:
        print "empty quote"
        bashquote(random.randint(7,963184))
    else:
        print "quote_tbc is of type: " + str(type(quote_tbc))
        yield quote_tbc
