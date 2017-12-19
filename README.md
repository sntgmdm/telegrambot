# telegrambot
Telegram Bot for my Rasberry Pi acting as TorrentBox

This should work as monitoring for the TorrentBox that will be unaccesible.
Plus why not some fun with Bots! :)

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
