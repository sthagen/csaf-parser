# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Parse CSAF v2.0 as well as CVRF v1.x documents and report the requested aspects."""
import os
import sys

DEBUG_VAR = "CSAF_DEBUG"
DEBUG = os.getenv(DEBUG_VAR, '')


def main(argv=None):
    """Drive the validator."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print("ERROR arguments expected.", file=sys.stderr)
        return 2
    DEBUG and print("DEBUG: argv =", argv)
