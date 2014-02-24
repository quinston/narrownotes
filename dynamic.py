import os
import sys

folderName = sys.argv[1]
texFiles = filter(lambda x: '.tex' == x[-4:], os.listdir(folderName))
exclusions = []
for exclusion in exclusions: texFiles.remove(exclusion)
for texFile in sorted(texFiles):
	print '\input{{{}}}'.format(folderName + "/" + texFile)
