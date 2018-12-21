#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import re
import sys


def get_words(text_file_name):
    words = set()
    with open(text_file_name, 'r') as text_file:
        for line in text_file:
            line_words = re.findall(r'\b\w+\b', line)
            words.update(set(line_words))
    return words


def make_uniq_name(text_file_name):
    text_file = Path(text_file_name)
    dir_name = text_file.parent
    file_name = text_file.name
    file_ext = text_file.suffix
    new_file_name = Path(file_name.replace(file_ext,
                                           '_uniq' + file_ext))
    return str(dir_name / new_file_name)

if __name__ == '__main__':
    arg_parser = ArgumentParser(description='find distinctive '
                                            'words in a text')
    arg_parser.add_argument('file', help='text file to process')
    arg_parser.add_argument('--corpus', help='file glob for '
                                             'the corpus')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output for debugging')
    options = arg_parser.parse_args()
    file_words = get_words(options.file)
    corpus_words = set()
    for file in Path.cwd().glob(options.corpus):
        if options.verbose:
            print(f'processing {file}', file=sys.stderr)
        if file == Path.cwd() / Path(options.file):
            if options.verbose:
                print('skipping file', file=sys.stderr)
            continue
        words = get_words(file)
        corpus_words.update(set(words))
    uniq_words = file_words - corpus_words
    if uniq_words:
        with open(make_uniq_name(options.file), 'w') as uniq_file:
            print(' '.join(uniq_words), file=uniq_file)
    else:
        print(f'{options.file}: no unique words',
              file=sys.stderr)
