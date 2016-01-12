---- slave script ----
#!/bin/sh

SERVICE='omxplayer-sync'
while true; do
if ps ax | grep -v grep | $SERVICE > /dev/null
then
echo "running" #>>/dev/null
else
omxplayer-sync -b -l /home/pi/Desktop/SyncPi8/synctest.mp4 &

fi
done

---- end slave script ----
