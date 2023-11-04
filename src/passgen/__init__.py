import secrets
import string
import sys

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def cli():
    parsed_args = _parse(sys.argv[1:])
    print(generate_password(parsed_args.length, parsed_args.include_symbols))


def generate_password(length, include_symbols=False):
    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation

    return ''.join(secrets.choice(alphabet) for _ in range(length))


def _parse(args):
    parser = ArgumentParser(
        description='passgen',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        'length',
        type=int,
        nargs='?',
        default=32,
    )
    parser.add_argument(
        '-s',
        '--include-symbols',
        help='include symbols',
        default=False,
        action='store_true',
    )
    return parser.parse_intermixed_args(args)
