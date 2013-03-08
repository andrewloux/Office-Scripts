# Multiple Files Version
# Windows ONLY. line 34 fails on Linux, will look into the cause.

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Merge numerical data in all the \
                                 text files within a folder, sort, and then \
                                 dump into one big text file')
parser.add_argument('-s',
                    '--source directory',
                    help='Folder containing source text files.',
                    required=True)
parser.add_argument('-d',
                    '--destination directory',
                    help='Destination directory of operation.',
                    required=True)
parser.add_argument('-st',
                    '--starting file',
                    help='Select any data text file within source folder.',
                    required=True)

args = vars(parser.parse_args())

path = args['source directory']  # Source path
output = args['destination directory'] + '/NewFile.txt'

outfile = open(output, 'w')
counter = 0

lines = file(args['starting file']).readlines()[1:]

for files in os.listdir(path):
    if counter == 2:
        lines.sort(key=lambda x: float(x.split()[0]))
        for line in lines:
            outfile.write(line)
        outfile.close()
        Proceed = raw_input('Check your output file. If you want to proceed, \
                            hit Y, otherwise hit N\n')
        if Proceed == 'Y':
            counter = 0
            outfile = open(output, 'w')
            lines += file(str(path) + '/' + str(files)).readlines()[1:]
        elif Proceed == 'N':
            sys.exit()
    else:
        counter += 1
        lines += file(str(path) + '/' + str(files)).readlines()[1:]

for line in lines:
    outfile.write(line)

outfile.close()
