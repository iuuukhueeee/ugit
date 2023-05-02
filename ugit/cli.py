import argparse


def init(args):
    print('Goodbye World')


def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(default_function=init)

    return parser.parse_args()


def main():
    args = parse_args()
    print(args, end='\n')
    args.default_function(args)
