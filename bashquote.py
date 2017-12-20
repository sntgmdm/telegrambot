from lxml import html
import requests

def bashquote( randnum ):
    bash = requests.get('http://bash.org/?' + str(randnum))
    bashtree = html.fromstring(bash.content)

    quote = bashtree.xpath('//p[@class="qt"]/text()')
