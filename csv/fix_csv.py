#! /usr/local/bin/python3
import sys
import csv

old_filename, new_filename = sys.argv[1:]

with open(old_filename, newline="") as old_file:
    rows = list(csv.reader(old_file, delimiter="|"))

with open(new_filename, mode="wt", newline="") as new_file:
    csv.writer(new_file).writerows(rows)
