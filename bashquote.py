from lxml import html
import requests
import random

def bashquote( randnum ):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)
    quote = bashtree.xpath('//p[@class="qt"]/text()')
    quote_text = quotechequer(quote)
    quote_result = quote_text
    print "quote_result is of type: " type(quote_result)
    yield quote_result

def quotechequer ( quote_tbc ):
    if not quote_tbc:
        print "empty quote"
        bashquote(random.randint(7,963184))
    else:
        yield quote_tbc
