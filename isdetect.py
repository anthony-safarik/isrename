#helper functions to check information about image sequences
import os
import re

def check_sequential(sequence,delimiter):
    # enter a list of file names and the frame number delimiter character
    # returns True or False
    previous_frame_number = None
    is_continuous = False
    for item in sequence:
        fname,ext = os.path.splitext(item)
        split_fname = fname.split(delimiter)
        frame_number = split_fname[-1]
        if frame_number.isdigit():
            frame_number = int(frame_number)
        else:
            break
        if previous_frame_number:
            if frame_number - previous_frame_number == 1:
                is_continuous = True
            else:
                is_continuous = False
                break
        previous_frame_number = frame_number
    return is_continuous


delimiter = '.'
sequence = []
for fname in sorted(os.listdir('testing')):
    if fname.endswith('.dpx'):
        sequence.append(fname)

files_are_sequential = check_sequential(sequence, delimiter)
print (files_are_sequential)
