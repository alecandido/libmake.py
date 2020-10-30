import argparse

from .makefile import Makefile
from .globals import rule_vars, make_vars


def run_make(makefile):
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="*")
    args = ap.parse_args()
    makefile.run(args.targets)
