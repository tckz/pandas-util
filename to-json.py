#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# JSON lines

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_table(fn)

df.to_json(sys.stdout, orient='records', force_ascii=False, lines=True)
