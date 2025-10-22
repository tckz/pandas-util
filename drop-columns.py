#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# 列を削除

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--column", action="append", required=True)
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)
df = df.drop(args.column, axis=1)

df.to_csv(sys.stdout, sep="\t", index=False)
