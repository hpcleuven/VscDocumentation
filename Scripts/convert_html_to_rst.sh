#!/usr/bin/env bash

for file in output/*.html
do
    pandoc -f html -t rst -o "${file/html/rst}" "${file}"
done
