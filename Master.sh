#---- master script ----

#!/bin/sh

SERVICE='omxplayer-sync'
while true; do
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
echo "running" #>>/dev/null
else
omxplayer-sync -b -m /home/pi/SyncPi8/SyncVideo.mp4 &

fi
done

#---- end master script ----
