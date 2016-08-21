#											 #
# Removes all leading non-alphabetical characters in all files in the current directory  #
#											 #	

import os
stop = False

def isalpha(x):
	"""Returns true if character passed in is alphabetical"""

	if x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
		return True
	else:
		return False

for filename in os.listdir("."):
	num = -1
	for c in filename:
		if stop:
			stop = False
			break
		num += 1
		if isalpha(c):
			os.rename(filename, filename[num:])
			num = 0
			stop = True

