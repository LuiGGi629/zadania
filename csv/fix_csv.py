#! /usr/local/bin/python3
from argparse import ArgumentParser
import csv

parser = ArgumentParser()
parser.add_argument("old_filename")
parser.add_argument("new_filename")
parser.add_argument("--in-delimiter", dest="delim")
parser.add_argument("--in-quote", dest="quote")
args = parser.parse_args()

with open(args.old_filename, newline="") as old_file:
    quotechar = '"'
    delimiter = '|'
    if args.delim:
        delimiter = args.delim
    if args.quote:
        quotechar = args.quote
    reader = csv.reader(old_file, delimiter=delimiter, quotechar=quotechar)
    rows = list(reader)

with open(args.new_filename, mode="wt", newline="") as new_file:
    csv.writer(new_file).writerows(rows)
