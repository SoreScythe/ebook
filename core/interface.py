## module to parse the arguments
from sys import argv
import argparse

parser = argparse.ArgumentParser(
                        prog="Ebook Author",
                        description="A simp",
                        epilog="please use wisely for the author is not so smart"
)
parser.add_argument('-o', '--output', required=True, help="path to the output file", type=str)
parser.add_argument('-t', '--title', required=True, help="book title", type=str)
args = parser.parse_args(argv[1:])