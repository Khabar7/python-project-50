import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('strings', metavar='first_file', type=str, nargs=1,
                    help='')
parser.add_argument('strings', metavar='second_file', type=str, nargs=1,
                    help='')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()
