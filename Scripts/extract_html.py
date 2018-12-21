#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import re


def main():
    arg_parser = ArgumentParser(description='convert dump to files')
    arg_parser.add_argument('file', help='dump file to convert')
    arg_parser.add_argument('--dir', default='output',
                            help='name of output directory')
    options = arg_parser.parse_args()
    output_dir = Path(options.dir)
    if not output_dir.exists():
        output_dir.mkdir()
    with open(options.file, 'r') as input_file:
        _ = input_file.readline()
        content = None
        id = None
        title = None
        for line in input_file:
            match = re.match(r'^(\d+),\"(.*?)\",(.*)$', line)
            if match:
                print(f'{match.group(1)}: {match.group(2)}')
                if content is not None:
                    output_path = output_dir / f'file_{int(id):04d}.html'
                    content = content.strip('"')
                    if content:
                        with output_path.open('w') as output_file:
                            if title:
                                print(f'<h1>{title}</h1>', file=output_file)
                            print(content, file=output_file)
                id = match.group(1)
                title = match.group(2)
                content = match.group(3)
            else:
                content += line


if __name__ == '__main__':
    main()
