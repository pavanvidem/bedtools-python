#!/usr/bin/env python

import unittest
import os

from bedtools import Interval, IntervalFile

def main():
    """
    Print each BED feature in a BED file.
    """    
    for exon in IntervalFile("bedtools/tests/data/exons.hg18.chr21.bed"):
        print exon



if __name__ == "__main__":
    main()