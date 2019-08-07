#!/usr/bin/env bash

for file in output/*.rst
do
    ./compute_distinct_words.py --corpus 'output/*.rst' "$file"
done
