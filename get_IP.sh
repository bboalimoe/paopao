#!/bin/bash

IP=`curl ifconfig.me`;

git pull;

if [ $? -ne 0 ]
then
echo "git pull error!"
exit 1;
fi

if [ -e /home/niuben/paopao/Server_IP.txt ]
then
echo $IP > /home/niuben/paopao/Server_IP.txt;
fi

git add Server_IP.txt;

update_time=`date "+%Y-%m-%d %H:%M:%S"`;

git commit Server_IP.txt -m "rebot. update Server IP at $update_time";

git push -u origin master;

if [ $? -eq 0 ]
then
echo "+++++++++++++++++     [ok]";
fi
