#Filename:cat.py

import sys

def readfile(filename):
	'''Print a file to the standard output.'''
	f=file(filename)
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print line,
	f.close()

#Script starts from here
if len(sys.argv)<2:
	print 'No action specified.'
	sys.exit()
	
if sys.argv[1].startswith('--'):
	option=sys.argv[1][2:] #sys.argv[1][2:]后面的括号是分割字符串
	#fecth sys.argv[1] but without the first two characters.
	if option=='version':
		print 'Version 1.2'
	elif option=='help':
		print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
	--Verson:Prints the version number
	--help  :Display the help'''
	else:
		print 'Unknown option'
	sys.exit()
else:
	for filename in sys.argv[1:]:
		readfile(filename)