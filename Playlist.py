import sys,os,subprocess,argparse

#Command line parser
parser = argparse.ArgumentParser(description='A quick and dirty way to create a living youtube playlist downloader')
parser.add_argument('-p','--path of Playlist.txt', help='Path of Playlist.txt file and folder', required=True)
args = vars(parser.parse_args())
os.chdir(args['path of Playlist.txt'])
playlist = open ("Playlist.txt",'r')
for line in playlist.readlines():
      subprocess.call(['youtube-dl',line])
