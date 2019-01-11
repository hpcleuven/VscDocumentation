#!/usr/bin/env bash

for file in *.rst
do
    less "$file"
    read -p "move [ajs]?" -n 1 -r
    if [[ $REPLY =~ ^[aA]$ ]]
    then
        dir='access'
    elif [[ $REPLY =~ ^[jJ]$ ]]
    then
        dir='jobs'
    elif [[ $REPLY =~ ^[sS]$ ]]
    then
        dir='software'
    else
        continue
    fi
    git mv "$file" "$dir/$file"
done
