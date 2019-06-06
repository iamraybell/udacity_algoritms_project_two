## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))

# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))

# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))


def findFile(pathSoFar , endswith = '.c' ):
    outputList = []
    def checkDir(pathSoFar, endswith, outputList): 
        if os.path.isdir(pathSoFar) :
            for item in os.listdir(pathSoFar):
                checkDir(pathSoFar + '/' + item, endswith, outputList)

        if os.path.isfile(pathSoFar):
            if pathSoFar.endswith(endswith):
                outputList.append(pathSoFar)
    checkDir(pathSoFar, endswith, outputList)
    return outputList

print(findFile('./testdir'))
print('********************')
print(findFile('./testdir', '.h'))
print('********************')
print(findFile('./testdir', '.12233444'))
print(findFile('./testdir', '.gitkeep'))
print(findFile('./this is not a real directory!', '.gitkeep')) # should not find anything, since this isnt a real directory!




