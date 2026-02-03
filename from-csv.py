#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", required=False)
args = arg_parser.parse_args()

fn = sys.stdin if args.input is None else args.input

df = pd.read_csv(fn)

df.to_csv(sys.stdout, sep="\t", index=False)
