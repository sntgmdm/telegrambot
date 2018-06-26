from lxml import html
import requests
import random

def bashquote(randnum,chat_id):
    #select a random quote page (1-422)
    pre_bash = requests.get('http://bash.org/?browse&p=' + str(randnum))
    pre_bashtree = html.fromstring(pre_bash.content)
    #list of all quote numbers of the random site
    pre_quote_nums = pre_bashtree.xpath('//p[@class="quote"]/a/b/text()')
    #select one item from the lsit. it's in the #XXXXXXXXX format we need to remove the #
    quote_pre = pre_quote_nums[random.randint(0,len(pre_quote_nums)-1)]
    #type should be string
    quote = quote_pre[1:]
    bash = requests.get('http://bash.org/?' + quote)
    bashtree = html.fromstring(bash.content)
    quote_text = bashtree.xpath('//p[@class="qt"]/text()')
    #save the quote number and sender in the logfile
    bashlog = open('bash.log', 'a')
    bashlog.write('Quote number #' + quote + ' served to: ' +str(chat_id) + '\n')
    bashlog.close()
    #finaly retrun the quote to the main loop
    return quote_text
