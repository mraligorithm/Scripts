#!/bin/bash
#At times, we need to monitor the high CPU usage in the system. 
#We can use the below script to monitor the high CPU usage.
while [ true ] ;do
used=`free -m |awk 'NR==3 {print $4}'`

if [ $used -lt 1000 ] && [ $used -gt 800 ]; then
echo "Free memory is below 1000MB. Possible memory leak!!!" | /bin/mail -s "HIGH MEMORY ALERT!!!" user@mydomain.com


fi
sleep 5
done