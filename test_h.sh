#!/usr/bin/env bash

DATE=$(date)

cd ~/Documents/Github/small_projects

git add .
git commit -m "changes made on $DATE"
git push

echo Think it worked