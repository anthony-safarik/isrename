#!/usr/bin/env python
import os
import argparse

parser = argparse.ArgumentParser(description='This script renames image sequences')
parser.add_argument('-i','--inpath', help='folder path containing an image sequence',required=True)
parser.add_argument('-e','--ext', help='file extension to operate on',required=True)
parser.add_argument('-t','--target', help='target is the new name for the sequence',required=False)
parser.add_argument('-s','--start', help='start frame number',required=False)
parser.add_argument('-d','--delimiter', help='frame number delimiter',required=False)

args = parser.parse_args()

#set the required variables
inpath = args.inpath
ext = args.ext

#test validity of inpath
try:
    print(inpath)
    assert os.path.isdir(inpath), "inpath is not a valid directory"
except AssertionError as e:
    print(e)
    quit()

#set unrequired variables to defaults
if not args.start:
    start = '00001'
else:
    start = args.start
    for i in start:
        if not i.isdigit():
            print (start,'contains non-digits... setting the start frame to 00001')
            start = '00001'
            break

if not args.target:
    print ('no name provided, defaulting to parent folder name')
    target = os.path.basename(inpath)

# "." is the default delimiter if user doesn't provide one
if type(args.delimiter) is str:
    frame_number_delimiter = args.delimiter
else:
    frame_number_delimiter = '.'

if not ext.startswith('.'):
    ext = '.'+ext

print ('inpath='+inpath,'ext='+ext,'start='+start)

def rename_sequence(inpath,ext,start_frame,target_name,frame_number_delimiter):
    '''inpath is a folder of files of extension "ext" to be renamed to target_name.
    start_frame is a string containing digits only, padded with zeroes to match desired target_name frame number padding'''

    padding = len(start_frame)
    frame_count = int(start_frame) - 1

    for fname in sorted(os.listdir(inpath)):

        fname_base, fname_ext = os.path.splitext(fname)

        if ext == fname_ext:
            frame_count+=1
            target_frame_number = str(frame_count).zfill(padding)
            target_name_full = target_name + frame_number_delimiter + target_frame_number + ext
            print (fname_base,'>',target_name_full)


rename_sequence(inpath,ext,start,target,frame_number_delimiter)
