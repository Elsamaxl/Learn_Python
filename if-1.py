#Filename:if-1.py
number=23
guess=int(raw_input('Please input a integer:'))
if guess==number:
	print('You guess it')
else :
	if guess<number:
		print('It a little bigger than that')
	else :
		if guess>number:
			 print('It a little lower than that' )
print('Done')
