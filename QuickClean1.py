#!/usr/bin/env python
#Quickly clean my music, videos and images into a different directory.
#QuickClean.py
#Version 0.02
import glob
import sys
import os
import shutil
import argparse


parser = argparse.ArgumentParser(description='A quick way to clean out your cluttered folders.')
parser.add_argument('-s','--source', help='Directory you want to clean out. If no other argumnets are provided, will create relevant directories under source directory', required=True)
parser.add_argument('-m','--music', help='Directory you want to copy music files to. If absolute path is not provided, will create directory inside the source directory', default='music', required=False)
parser.add_argument('-p','--pictures', help='Directory you want to copy picture files to. If absolute path is not provided, will create directory inside the source directory', default='pictures', required=False)
parser.add_argument('-v','--videos', help='Directory you want to copy video files to. If absolute path is not provided, will create directory inside the source directory', default='videos', required=False)
parser.add_argument('-d','--documents', help='Directory you want to copy document files to. If absolute path is not provided, will create directory inside the source directory', default='documents',required=False)


args = parser.parse_args()
os.chdir(args.source)


#Parameters to clean.
music = glob.glob("*.mp3") + glob.glob("*.flac") + glob.glob("*.aac")
pictures = glob.glob("*.png") + glob.glob ('*.jpg') + glob.glob("*.bmp")+ glob.glob("*.gif")
videos = glob.glob("*.avi") + glob.glob("*.mp4") + glob.glob("*.flv") + glob.glob("*.mkv") + glob.glob("*.mov")
documents = glob.glob ('*.pdf') + glob.glob ('*.PDF') + glob.glob ("*.xls") + glob.glob ("*.xlsx") + glob.glob ("*.pptx") + glob.glob ("*.docx") + glob.glob("*.m") + glob.glob("*.ppt") + glob.glob("*.doc")

   
#Copies to destination directory, and then deletes the file. This is done because shutil's copy method has the ability to overwrite. 
for songs in music:
	if not os.path.exists(args.music):
		os.mkdir(args.music)
	shutil.copy(songs,args.music)
	os.remove(songs)
for video in videos:
	if not os.path.exists(args.videos):
		os.mkdir(args.videos)
	shutil.copy(video,args.videos)
	os.remove(video)
for picture in pictures:
	if not os.path.exists(args.pictures):
		os.mkdir(args.pictures)
	shutil.copy(picture,args.pictures)
	os.remove(picture)
for document in documents:
	if not os.path.exists(args.documents):
		os.mkdir(args.documents)
	shutil.copy(document,args.documents)
	os.remove(document)

