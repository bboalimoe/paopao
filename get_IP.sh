#!/bin/bash

branch_cur=`git branch | grep '*' | awk '{print $2}'`
echo "branch is $branch_cur"
git stash
git checkout ip_realtime

if [ $? -eq 0 ]
then
curl ifconfig.me -o README.md
ip=`cat README.md`;
update_time=`date "+%Y-%m-%d %H:%M:%S"`;

git add README.md;
git commit -m "wlan IP $ip update at $update_time";
git push -f origin ip_realtime;
fi
git checkout $branch_cur
git stash pop
