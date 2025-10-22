#!/usr/bin/env python3

import argparse
import sys

import pandas as pd

# concatした結果を返す

# --direction=v: 縦方向（行追加）
# --direction=h: 横方向（列追加）

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", action="append", required=False)
arg_parser.add_argument("--direction", default="v", choices=["v", "h"])
arg_parser.add_argument("files", nargs=argparse.REMAINDER)
args = arg_parser.parse_args()

files = (args.input or []) + args.files
if len(files) == 0:
    files = [sys.stdin]

df = pd.concat([pd.read_table(e) for e in files], axis=0 if args.direction == "v" else 1)

df.to_csv(sys.stdout, sep="\t", index=False)
