import os, fnmatch, collections 
from dblogic import report_reindex



def report_reindex_igniter():
	exlist = ['*.xdo']

	for root, directories, filenames in os.walk('./original/'):
		for extensions in exlist:
			for filename in fnmatch.filter(filenames, extensions):
				title = (os.path.join(filename)).replace(".xdo", "")
				report_directory = (os.path.join(root))
				file_name = (os.path.join(filename))
				report_reindex(title, report_directory, file_name)

def template_reindex_igniter():
	