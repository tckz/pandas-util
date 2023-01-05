#!/usr/bin/env python3

import argparse
import sys

import pandas as pd
from tabulate import tabulate

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--input', required=False)
args = arg_parser.parse_args()

fn = args.input
if fn is None:
    fn = sys.stdin

df = pd.read_table(fn)

print(tabulate(df, showindex=False, headers=df.columns))
