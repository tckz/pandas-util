#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# 指定の列だけ抜き出す

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--column", action="append", required=True)
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = args.input
if fn is None:
    fn = sys.stdin

df = pd.read_table(fn)
df = df[args.column]

print(df.to_csv(sep="\t", index=False), end="")
