import os, re

# Enter the path you want to look through
placepathhere = input('Enter the path you want to check: ')
fileinfo = os.stat(placepathhere)

"""
Specs Requested
===============
find directories called - Full diff log
list of the diffed difference
And anything new that does not match the previous list

"""

def backuppath():
    for dirname, dirnames, filenames in os.walk(placepathhere, topdown=False, onerror=None, followlinks=False):
    # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

    # print path to all filenames.
        for filename in filenames:
            print(str(fileinfo), os.path.join(dirname, filename,))


backuppath()



