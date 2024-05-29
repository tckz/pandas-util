#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# --query 'ignore_webhook!=True'

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--query", required=True)
arg_parser.add_argument("--input", required=False)
arg_parser.add_argument("--engine", required=False)
args = arg_parser.parse_args()

fn = args.input
if fn is None:
    fn = sys.stdin

df = pd.read_table(fn)
df = df.query(args.query, engine=args.engine)

print(df.to_csv(sep="\t", index=False), end="")
