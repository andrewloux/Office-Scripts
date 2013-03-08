#!/usr/bin/python

# Created by Andrew Louis, Febraury 21, 2013
# You may use this script under the MIT License. All Rights Reserved

import re
import argparse

# Command line parser.
parser = argparse.ArgumentParser(description='A quick way to scrub the census \
                                 data could be found here: http://www12.statcan.gc.ca/english/census06/data/popdwell/File.cfm?T=307&SR=1&RPP=699&PR=0&CMA=0&S=3&O=D&LANG=E&OFT=CSV')
parser.add_argument('-s',
                    '--path of raw csv data',
                    help='Folder holding raw census data.',
                    required=True)
parser.add_argument('-d',
                    '--path of destination text file',
                    help='Destination folder',
                    required=True)

args = vars(parser.parse_args())

thelist = list()
with open(args['path of raw csv data'], 'r') as f:
    for line in f:
        if line[1].isdigit():
            city = re.findall("\"(.*?)\s*\(", line)
            population = re.findall(",([0-9]*),", line)
            if population:
                x = population[0]
                thelist.append([city, x])
            
with open(args['path of destination text file'], 'w') as g:
    for item in thelist:
        string = item[0], ', '.join(map(str, item[1:]))
        string = string[0][0] + ' ' + string[1] + '\n'
        g.write(string)
