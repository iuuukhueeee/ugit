import argparse
import os
from . import data


def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(default_function=init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(default_function=hash_object)
    hash_object_parser.add_argument('file')

    return parser.parse_args()


def init(args):
    if data.init():
        print(
            f'Initialized empty ugit respository in {os.getcwd()}/{data.GIT_DIR}')


def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))


def main():
    args = parse_args()
    print(args, end='\n')
    args.default_function(args)
