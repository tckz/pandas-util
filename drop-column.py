#!/usr/bin/env python3

import argparse
import sys
from functools import reduce

import pandas as pd

# 列を削除

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--column", action="append", required=True)
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = args.input
if fn is None:
    fn = sys.stdin

df = reduce(lambda a, b: a.drop(b, 1), args.column, pd.read_table(fn))

print(df.to_csv(sep="\t", index=False), end="")
