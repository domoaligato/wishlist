#!/usr/bin/env python

from wishlist.core import Wishlist
import sys, getopt

def main(argv):
    inputwishlist = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["i="])
    except getopt.GetoptError:
        print ('wishlist2csv.py -i <inputwishlist>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('wishlist2csv.py -i <inputwishlist>')
            sys.exit()
        elif opt in ("-i"):
            inputwishlist = arg
    name = inputwishlist
    w = Wishlist(name)
    print('"'+'title'+'"'+','+'"'+'url'+'"')
    for item in w:
        we_json = item.jsonable()
        print('"'+we_json["title"]+'"'+","+'"'+we_json["url"]+'"')
if __name__ == "__main__":
   main(sys.argv[1:])

# example wishlist id 9I87I1RYLTAA
# This is just a quick version of the wishlist script to export amazon wishlists to csv.


