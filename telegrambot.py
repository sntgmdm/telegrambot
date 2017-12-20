import os
import sys
import time
import random
import datetime
import getip
import telepot
from telepot.loop import MessageLoop
from uptime import uptime
from bashquote import bashquote

light = False

def handle(msg):
    global light
    chat_id = msg['chat']['id']
    command = msg['text']


    print 'Got command: '+ command + ' from: ' + str(chat_id)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/spitip':
        bot.sendMessage(chat_id, str(getip.get()))
    elif command == '/uptime':
        uptimemessage = 'The system uptime is: ' + uptime()
        bot.sendMessage(chat_id, uptimemessage)
    elif command == '/aziz':
        light = not(light)
        if light:
            bot.sendMessage(chat_id, 'Good boy Aziz')
        else:
            bot.sendMessage(chat_id, 'Aziz light!!!')
    elif command == '/bash':
        quote_tbs = bashquote(random.randint(7,963184))
        for quote_sentence in quote_tbs:
            bot.sendMessage(chat_id, quote_sentence)
    else:
        bot.sendMessage(chat_id, 'I did not understand you')

bottoken = open('/home/pi/teletorrentbottoken.txt', 'r').read().splitlines()
bot = telepot.Bot(bottoken[0])


MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
