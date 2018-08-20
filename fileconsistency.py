import shutil
import os

targetdir = "out/RU/01 Accounts/0101 Account balance/"
targetdirs = [{'dir':'out/RU/01 Accounts/0101 Account balance/'},{'dir':'out/RU/02 Accounts2/0102 Account balance/'}]
lang_id = 1

for a in targetdirs:	
	if not os.path.exists(a['dir']):
	    os.makedirs(a['dir'])