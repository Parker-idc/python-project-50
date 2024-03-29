import argparse


DESCRIPTION = "Compares two configuration files and shows a difference."
HELP = "set format of output"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", type=str, default='stylish',
                        choices=['stylish', 'plain', 'json'], help=HELP)

    args = parser.parse_args()
    return args
