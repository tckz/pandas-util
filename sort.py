#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--column', action='append', required=True)
arg_parser.add_argument('--direction', action='append', required=False)
arg_parser.add_argument('--input', required=False)
args = arg_parser.parse_args()

fn = args.input
if fn is None:
    fn = sys.stdin

df = pd.read_table(fn)
asc = args.direction
if asc is None:
    asc = True
else:
    asc = [x == 'asc' for x in args.direction]

# stableにするためにmergesort
df = df.sort_values(by=args.column, ascending=asc, kind='mergesort')

print(df.to_csv(sep='\t', index=False), end='')
