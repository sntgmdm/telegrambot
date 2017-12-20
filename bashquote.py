from lxml import html
import requests
import random

def bashquote( randnum ):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)
    quote = bashtree.xpath('//p[@class="qt"]/text()')
    quotechequer(quote)

def quotechequer ( quote_tbc ):
    if not quote_tbc:
        bashquote(random.randint(7,963184))
    else:
        print quote_tbc

bashquote(random.randint(7,963184))
