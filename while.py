#Filename:while.py

number=43
running=Ture
while running
	guess=int(raw_input('Enter an integer:'))
	if guess==number:
		print 'Congratulations,you guessed it.'
		running=False #this causes the whlie loop to stop
	elif guess>number:
		print 'No,it is a little lower than that.'
	else :
		print 'No,it is a little higher than that.'
else :
	print 'The loop is over.'
	#Do anything else you want to do here.
print 'Done.'