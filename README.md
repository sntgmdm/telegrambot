# telegrambot
Telegram Bot for my Rasberry Pi acting as TorrentBox

This should work as monitoring for the TorrentBox that will be unaccesible.
Plus why not some fun with Bots! :)

Using telepot
Based on these instructions: http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/

On my Rasberry, when updating the code I use:
#git fetch --all
#git reset --hard origin/master

this way I just have to add the chatbot TOKEN

forget the old ways! the token is stored in a separate file in the /home/pi folder, now I cann just:
#git pull

to run the program in the background add '&' in the background
to kill the python process:
1st find the process id (PID)
#ps -ef | grep python
2nd kill the PID
#kill -9 2430

list of bot commands commands:
roll - Roll 1d6
time - Report current time
spitip - Blurt the current public IP
uptime - Give the total uptime
aziz - Play with Aziz and feel like exploring an alien cave
