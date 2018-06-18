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
import subprocess
import shlex
light = False
REBOOT_CHECK = False

resetpassfile = open('/home/pi/rebootpassword.txt', 'r')
RESETPASS = resetpassfile.read().splitlines()
resetpassfile.close()

localclientpwdfile = open('/home/pi/delugelocalclient.txt', 'r')
LOCALCLIENTPWD = localclientpwdfile.read().splitlines()
localclientpwdfile.close()

def handle(msg):
    global light
    global REBOOT_CHECK, RESETPASS
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
        bot.sendMessage(chat_id, "Be patient I'm choosing a random quote!")
        #422 is the last site of all quotes in bash.org
        quote_tbs = bashquote(random.randint(1,422),chat_id)
        bot.sendMessage(chat_id, "The quote is:")
        for quote_sentence in quote_tbs:
            bot.sendMessage(chat_id, quote_sentence)
    elif command == '/help' or command == '/?':
        bot.sendMessage(chat_id, '/help - Lists these commands below (/?) is also accepted\n' +
        '/bash - Grabs a quote from bash.org and send it you\n' +
        '/time - Report current time\n' +
        '/spitip - Blurt the current public IP\n' +
        '/uptime - Give the total uptime\n' +
        '/aziz - Play with Aziz and feel like exploring an alien cave\n' +
        '/roll - Roll 1d6')
    elif command == '/reboot':
        bot.sendMessage(chat_id, 'Enter the reboot password at any time')
        REBOOT_CHECK = True
    elif command == RESETPASS[0] and REBOOT_CHECK:
        bot.sendMessage(chat_id, 'Rebooting now')
        os.system('reboot')
    elif command == '/torrentstatus':
        command = shlex.split('deluge-console "conect 127.0.0.1:58846 localclient '+ LOCALCLIENTPWD[0] +'; info ; exit"')
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = process.communicate()
        bot.sendMessage(chat_id, str(output))
    else:
        bot.sendMessage(chat_id, 'I did not understand you')

bottokenfile = open('/home/pi/teletorrentbottoken.txt', 'r')
bottoken = bottokenfile.read().splitlines()
bottokenfile.close()
bot = telepot.Bot(bottoken[0])

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
