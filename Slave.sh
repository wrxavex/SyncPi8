#---- slave script ----
#!/bin/sh

SERVICE='omxplayer-sync'
while true; do
now=$(date)
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
echo "$now SyncVideo Slave running" #>>/dev/null
else
echo "Error--$now"
omxplayer-sync -b -l /home/pi/SyncPi8/SyncVideo.mp4 &

fi
done

#---- end slave script ----