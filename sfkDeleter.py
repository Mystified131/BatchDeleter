#This code imports the necessary modules

import os
import re
import collections
import operator
 
for subdir, dirs, files in os.walk('E:\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".sfk") :
            os. remove(filepath) 

for subdir, dirs, files in os.walk('H:\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".sfk") :
            os. remove(filepath) 

print("")

print("The designated files have been removed. Thank you.")

print("")