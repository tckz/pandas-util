#!/usr/bin/env python3

import argparse
import sys

import pandas as pd
from tabulate import tabulate

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)

print(tabulate(df, showindex=False, headers=df.columns, tablefmt=args.format))
