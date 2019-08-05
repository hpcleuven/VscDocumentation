#!/usr/bin/env bash

for file in $(ls output/*.rst | grep -v uniq)
do
    less $file
    read -p "move [Yn]?" -n 1 -r
    if [[ $REPLY =~ ^[yY]$ ]]
    then
        mv $file selected/$(basename $file)
    fi
done
