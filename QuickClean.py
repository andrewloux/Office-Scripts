#!/usr/bin/env python

# QuickClean.py
# Version 0.04

"""
Quickly clean music, videos, images and documents into a different directory.
"""

import argparse
import glob
import os
import shutil


parser = argparse.ArgumentParser(description='A quick way to clean out your \
                                              cluttered folders.')
parser.add_argument('-s',
                    '--source',
                    help='Directory you want to clean out. If no other \
                          argumnets are provided, will create relevant \
                          directories under source directory',
                    required=True)
parser.add_argument('-m',
                    '--music',
                    help='Directory you want to copy music files to. If \
                          absolute path is not provided, will create \
                          directory inside the source directory',
                    default='music',
                    required=False)
parser.add_argument('-p',
                    '--pictures',
                    help='Directory you want to copy picture files to. If \
                          absolute path is not provided, will create \
                          directory inside the source directory',
                    default='pictures',
                    required=False)
parser.add_argument('-v',
                    '--videos',
                    help='Directory you want to copy video files to. If \
                          absolute path is not provided, will create \
                          directory inside the source directory',
                    default='videos',
                    required=False)
parser.add_argument('-d',
                    '--documents',
                    help='Directory you want to copy document files to. If \
                          absolute path is not provided, will create \
                          directory inside the source directory',
                    default='documents',
                    required=False)


args = parser.parse_args()
os.chdir(args.source)

file_types = {
    "music": ["mp3", "flac", "aac"],
    "pictures": ["png", "jpg", "bmp", "gif"],
    "videos": ["avi", "mp4", "flv", "mkv", "mov"],
    "documents": ["pdf", "xls", "xlsx", "pptx", "docx", "m", "ppt", "doc"],
}


all_files = glob.glob("*")

for label, types in file_types.iteritems():
    for ext in types:
        for fname in all_files:
            if fname.endswith("." + ext):
                try: 
                    os.mkdir(vars(args)[label])   
                except OSError:
                    pass
                shutil.copy2(fname, vars(args)[label])
                os.remove(fname)
