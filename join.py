#!/usr/bin/env python3

import argparse
from functools import reduce

import pandas as pd

# 同じ列名でjoinした結果を返す

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--input', action='append', required=True)
arg_parser.add_argument('--how', default='inner', choices=['outer', 'left', 'right', 'inner', 'cross'])
args = arg_parser.parse_args()

df = pd.read_table(args.input.pop(0))
df = reduce(lambda a, b: a.merge(pd.read_table(b), how=args.how), args.input, df)

print(df.to_csv(sep='\t', index=False), end='')
