#!/bin/bash

# cache current branch name to restore dev env
branch_cur=`git branch | grep '*' | awk '{print $2}'`
git stash

git checkout ip_realtime

curl ifconfig.me -o README.md

if [ $? -eq 0 ]
then
ip=`cat README.md`;
update_time=`date "+%Y-%m-%d %H:%M:%S"`;

git add README.md;
git commit -m "wlan IP $ip update at $update_time";
git push -f origin ip_realtime;
fi

# restore 
git checkout $branch_cur
git stash pop
