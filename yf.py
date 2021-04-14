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
import pprint
import yfinance as yf

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
        # Read yahoo finance
        ######################
 
        # get stock info
        stock = yf.Ticker("TSLA")
         
        #print(stock.info)
        #pprint.pprint(stock.info)

        # Open a file and manually create a csv file
        file_name = 'stock.csv'
        f = open(file_name, 'w+')  # overwrites existing file

        # create header line
        f.write('"key", "value"\n')

        for key,val in stock.info.items():
            if key[0] == 's':
                #print ("key = ", key)
                #key[1] = key[1].capitalize()
                print(f'key = {key.capitalize()} | value = {val}')
                f.write(f'"{key.capitalize()}", "{val}"\n')
            #print (key, "=>", val)

        
        f.close()

        # get historical market data
        #hist = json.loads(msft.history(period="5d"))
        #pprint.pprint(hist)

        #for key,val in hist:
            #print (key, "=>", val)


        #End main with no errors
        return 0    #All is well
 
    except Exception as err:
        sys.stderr.write('ERROR: %s' % str(err))
        return 1
 
    finally:
        print('\nCleaning up...')
 
        #if 'in_file' in locals() and isinstance(in_file, IOBase):       in_file.close()  # this makes sure that the file will get closed properly in case some unhandled error happened
        print('...Clean up complete!')
### (end) MAIN ### ---------------------------
       
 
if __name__ == '__main__':
    sys.exit(main())
