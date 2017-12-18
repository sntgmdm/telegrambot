import sys
import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    message_id = msg['id']
    message_chat = msg['chat']
    command = msg['text']

    print 'Got command: '+ command + ' from: ' + str(chat_id) + ' message_id ' + str(message_id) + ' message_chat ' + str(message_id)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    else:
        bot.sendMessage(chat_id, 'I did not understand you')

bot = telepot.Bot('*** INSERT TOKEN ***')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
