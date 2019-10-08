#! /usr/local/bin/python3
from argparse import ArgumentParser
import csv

parser = ArgumentParser()
parser.add_argument("old_filename")
parser.add_argument("new_filename")
parser.add_argument("--in-delimiter", dest="delim", default='|')
parser.add_argument("--in-quote", dest="quote", default='"')
args = parser.parse_args()

with open(args.old_filename, newline="") as old_file:
    reader = csv.reader(old_file, delimiter=args.delim, quotechar=args.quote)
    rows = list(reader)

with open(args.new_filename, mode="wt", newline="") as new_file:
    csv.writer(new_file).writerows(rows)
