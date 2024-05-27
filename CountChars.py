#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Domingos
#
# Created:     03-02-2015
# Copyright:   (c) Domingos 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from array import *

def main():
    charCount = array('i')
    for i in range(256):
        charCount.append(0)

    fileName = "C:\\Users\\Domingos\\Documents\\Temp\\To Process\\The Adventures of Sherlock Holmes - Temp.txt"
    f1 = open (fileName, "r")
    while True:
        c = f1.read(1)
        if not c:
          print "End of file"
          break
        i = ord(c)
        charCount[i]= charCount[i] + 1

    for i in range(256):
        print "For i = " + str(i) + ", CharCount is " + str(charCount[i])

    f1.close()

if __name__ == '__main__':
    main()
