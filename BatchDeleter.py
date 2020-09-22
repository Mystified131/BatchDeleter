#This code imports the necessary modules

import os
import re
import collections
import operator
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")) or (filepath.endswith(".sfk")):
            os. remove(filepath) 

print("")

print("Files have been removed. Thank you.")

print("")