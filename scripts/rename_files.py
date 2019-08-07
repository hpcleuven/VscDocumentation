#!/usr/bin/env python

from pathlib import Path
import re
import subprocess
import sys
import click


CONTEXT_SETTINGS = {
    'help_option_names': ('-h', '--help', '-?'),
}


def get_title(file_name):
    with open(file_name, 'r') as file:
        title_line = file.readline()
        title_underline = file.readline()
        if re.match(r'^\s*=+\s*$', title_underline):
            return title_line
        else:
            return None


def create_name(title, directory, ext):
    file_name = re.sub(r'\W', '_', title.lower())
    file_name = re.sub(r'_+', '_', file_name)
    file_name = file_name.strip('_')
    return directory / f'{file_name}.{ext}'


def create_copy_name(file_name):
    ext = file_name.suffix
    return file_name.parent / f'{file_name.stem}_copy{ext}'


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('directory')
@click.option('--ext', default='rst', help='file extension to filer on')
@click.option('--dryrun', is_flag=True, help='only report, do not rename')
@click.option('--verbose', is_flag=True, help='show output')
def rename_files(directory, ext, dryrun, verbose):
    '''script to rename reStructuredText files based on the title
    '''
    files = set()
    directory = Path(directory)
    for file_name in directory.glob(f'*.{ext}'):
        title = get_title(file_name)
        if title is not None:
            new_file_name = create_name(title, directory, ext)
            if new_file_name in files:
                print(f'W warning: duplicate file name: {new_file_name}',
                      file=sys.stderr)
                new_file_name = create_copy_name(new_file_name)
            files.add(new_file_name)
            if verbose or dryrun:
                print(f'{file_name} -> {new_file_name}')
            if not dryrun:
                try:
                    subprocess.run(['git', 'mv', file_name, new_file_name],
                                   check=True)
                except subprocess.CalledProcessError as error:
                    print(error, file=sys.stderr)


if __name__ == '__main__':
    rename_files()
