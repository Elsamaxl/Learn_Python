#Filename:continue.py
while True:
	s=raw_input('Enter Something:')
	if s=='quit':
		break
	elif len(s)<3:
		continue
	print 'Input is of sufficient length'

		