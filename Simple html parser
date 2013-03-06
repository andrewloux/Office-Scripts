import urllib2
import re
import urllib as ul
from PIL import Image
import time
import os
from bs4 import BeautifulSoup

#def using_soup(r):
#    sub_reddit=urllib2.urlopen(r).read()
#    soup=BeautifulSoup(sub_reddit)
#    for link in soup.find_all('a'):
#       if link==('http://www.reddit.com/*'):
#            print ('nope')
#        else:
#            print (link.get('href'))
    



def find_links(sub_r):
    sub_reddit=urllib2.urlopen(sub_r).read()
    found_links=re.findall("http://i.imgur.com/\w+.(?:jpg|gif|png)", sub_reddit)
    return found_links

def get_images(list_of_links):
    n=int(input("Please enter where you want the image numbers to start from "))
    for im in list_of_links:
        n+=1
        c=str(n)
        ul.urlretrieve(im, "i" + c + ".jpg")


def main():
    sub=input("Please Enter in the subreddit where you want the images from  ")
    #using_soup(sub)
    links=find_links(sub)
    get_images(links)

main()
