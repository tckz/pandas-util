#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# 列をrename

# --column=old_name,new_name

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--column", action="append", required=True)
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)
df.rename(columns={pair[0]: pair[1] for pair in [c.split(",") for c in args.column]}, inplace=True)

df.to_csv(sys.stdout, sep="\t", index=False)
