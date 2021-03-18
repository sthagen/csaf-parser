#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
""""Command line interface for the CSAF/CVRF parser and to requested reporting aspects."""
import sys

import csaf_parser.parse as csaf_parse


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    csaf_parse.main(argv)
