import sys
import os
import time
import random
import datetime
import getip
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    light = false

    print 'Got command: '+ command + ' from: ' + str(chat_id)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/spitip':
        bot.sendMessage(chat_id, str(getip.get()))
    elif command == '/aziz':
        if light:
            bot.sendMessage(chat_id, 'Good boy Aziz')
        else:
            bot.sendMessage(chat_id, 'Aziz light!!!')
        light = not light
    else:
        bot.sendMessage(chat_id, 'I did not understand you')

bottoken = open('/home/pi/teletorrentbottoken.txt', 'r').read().splitlines()
bot = telepot.Bot(bottoken[0])

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
