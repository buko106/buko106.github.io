#! /usr/bin/env python3
from urllib.parse import quote
import sys
from argparse import ArgumentParser

description = ""
parser = ArgumentParser(description=description)
parser.add_argument("--input", type=str)
parser.add_argument("--output", type=str)
args = parser.parse_args()

if args.input:
    in_fp = open(args.input ,"rt")
else:
    in_fp = sys.stdin

if args.output:
    out_fp = open(args.output ,"wt")
else:
    out_fp = sys.stdout


out_fp.write(quote(in_fp.read(), safe=""))
