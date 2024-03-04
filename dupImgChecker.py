from imutils import paths
import argparse
import time
import sys
import cv2
import os

def dhash(image,hashSize=8):
    resized=cv2.resize(image,(hashSize+1,hashSize))
    diff=resized[:,1:]>resized[:,:-1]
    return sum([2**i for (i,v) in enumerate(diff.flatten()) if v])

ap=argparse.ArgumentParser()
ap.add_argument("-a","-D:\\badriFiles\\6thsem\ML\imageDataset\\bar\haystack",
                required=True,help="dataset of images to search through (i.e., the haystack)")
ap.add_argument("-n","-D:\\badriFiles\\6thsem\ML\imageDataset\\bar\\needles",
                required=True,help="set of images we are searching for(i.e., needles)")
args=vars(ap.parse_args())

haystackPaths=list(paths.list_images(args["haystack"]))
needlePaths=list(paths.list_images(args["needles"]))

