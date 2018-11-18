from lxml import html
import requests
import random
import time
import datetime
import os

def bashquote(randnum,chat_id):
    #type the path where the bash.log will be if __name__ == '__main__':
    bashlog_path = os.path.join('/', 'home', 'pi', 'telegrambot', 'bash.log')
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
    bashlog = open(bashlog_path, 'a')
    bashlog.write('Quote number #' + quote + ' served to: ' +str(chat_id) + ' on: ' + str(datetime.datetime.now()) + '\n')
    bashlog.close()
    #finaly retrun the quote to the main loop
    return quote_text
