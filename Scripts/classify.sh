#!/usr/bin/env bash

for file in $(ls output/*.rst
do
    less $file
    read -p "move [ajs]?" -n 1 -r
    if [[ $REPLY =~ ^[aA]$ ]]
    then
        git mv $file access/$file
    elif [[ $REPLY =~ ^[jJ]$ ]]
        git mv $file jobs/$file
    elif [[ $REPLY =~ ^[sS]$ ]]
        git mv $file jobs/$file
    fi
done
