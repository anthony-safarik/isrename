#!/usr/bin/env python
import os
import argparse

parser = argparse.ArgumentParser(description='This script renames image sequences')
parser.add_argument('-f','--folder', help='folder path',required=True)

args = parser.parse_args()
print (args.folder)
