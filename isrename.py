#!/usr/bin/env python
import os
import argparse

parser = argparse.ArgumentParser(description='This script renames image sequences')
parser.add_argument('-i','--inpath', help='enter folder path containing an image sequence',required=True)
parser.add_argument('-e','--ext', help='enter the file extension to operate on',required=True)
parser.add_argument('-s','--start', help='start frame number',required=False)

args = parser.parse_args()

inpath = args.inpath
ext = args.ext
start = args.start

print (inpath,ext,start)
