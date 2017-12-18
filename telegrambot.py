import sys
import time
import random
import datetime
import ipgetter
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: '+ command + ' from: ' + str(chat_id)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/spitip':
        bot.sendMessage(chat_id, str(ipgetter.myip()))
    else:
        bot.sendMessage(chat_id, 'I did not understand you')

bot = telepot.Bot('*** INSERT TOKEN ***')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
