import os,fnmatch
import fnmatch

exlist = ['*.xdo']

for root, directories, filenames in os.walk('./original/'):
    for extensions in exlist:
        for filename in fnmatch.filter(filenames, extensions):
            print(os.path.join(root, filename))