#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# --query 'ignore_webhook!=True'

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--query", required=True, help="e.g. 'ignore_webhook!=True', 'col2>10', 'col1==\"abc\"'")
arg_parser.add_argument("--input", required=False)
arg_parser.add_argument("--engine", required=False, help="e.g. python, numexpr")
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)
df = df.query(args.query, engine=args.engine)

df.to_csv(sys.stdout, sep="\t", index=False)
