import os,fnmatch
import fnmatch
import collections



d={}
exlist = ['*.xdo']

for root, directories, filenames in os.walk('./original/'):
	for extensions in exlist:
		for filename in fnmatch.filter(filenames, extensions):
			d.update({os.path.join(root): os.path.join(filename)})
			#print(os.path.join(root, filename))

print(d)	
