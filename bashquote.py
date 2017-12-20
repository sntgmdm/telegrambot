from lxml import html
import requests
import random

def bashquote(randnum):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)
    quote = bashtree.xpath('//p[@class="qt"]/text()')
    if not quote:
        print "empty quote"
        return bashquote(random.randint(7,963184))
    else:
        yield quote
