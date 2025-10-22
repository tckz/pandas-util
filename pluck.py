#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# 指定の列だけ抜き出す

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--column", action="append", required=True)
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)
df = df[args.column]

df.to_csv(sys.stdout, sep="\t", index=False)
