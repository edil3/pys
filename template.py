#!/usr/bin/python3
 
__author__ = 'your name goes here'
 
 
"""
More comments here
 
"""
import os
import json
import string
import sys
import re
from io import IOBase
 
### GLOBALS ### ---------------------------
 
 
 
### FUNCTIONS ### ---------------------------
 
 
 
#
#
######################
# Main
######################
def main():
 
    # Global try / except clause
    try:
 
        ######################
        # Read txt file
        ######################
 
        # Open file
        in_file = open("test.txt")
       
        #Read first line from txt file
        txtline = in_file.readline().strip()  # strip whitespaces
       
        #Loop through all text lines and print each line
        while txtline:
            print(txtline)
            txtline = in_file.readline().strip()  # strip whitespaces
       
        # close file
        in_file.close()
 
        #End main with no errors
        return 0    #All is well
 
    except Exception as err:
        sys.stderr.write('ERROR: %s' % str(err))
        return 1
 
    finally:
        print('Cleaning up...')
 
        if 'in_file' in locals() and isinstance(in_file, IOBase):       in_file.close()  # this makes sure that the file will get closed properly in case some unhandled error happened
        print('...Clean up complete!')
### (end) MAIN ### ---------------------------
       
 
if __name__ == '__main__':
    sys.exit(main())
