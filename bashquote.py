from lxml import html
import requests
import random

def bashquote(randnum):
    #select a random quote page (1-422)
    pre_bash = requests.get('http://bash.org/?browse&p=' + str(randnum))
    pre_bashtree = html.fromstring(bash.content)
    #list of all quote numbers of the random site
    pre_quote_nums = bashtree.xpath('//p[@class="quote"]/a/b/text()')
    #select one item from the lsit. it's in the #XXXXXXXXX format we need to remove the #
    quote_pre = quote_nums[random.randint(0,len(quote))]
    #type should be string
    quote = quote_pre[1:]
    bash = requests.get('http://bash.org/?' + quote)
    bashtree = html.fromstring(bash.content)
    quote_text = bashtree.xpath('//p[@class="qt"]/text()')

    return quote_text
