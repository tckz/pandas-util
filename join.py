#!/usr/bin/env python3

import argparse
import sys
from functools import reduce

import pandas as pd

# 同じ列名でjoin（実体merge）した結果を返す

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", action="append", required=False)
arg_parser.add_argument("--how", default="inner", choices=["outer", "left", "right", "inner", "cross"])
arg_parser.add_argument("files", nargs=argparse.REMAINDER)
args = arg_parser.parse_args()

files = (args.input or []) + args.files
if len(files) == 0:
    files = [sys.stdin]

df = pd.read_table(files.pop(0))
df = reduce(lambda a, b: a.merge(pd.read_table(b), how=args.how), files, df)

df.to_csv(sys.stdout, sep="\t", index=False)
