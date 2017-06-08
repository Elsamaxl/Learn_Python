#Filename:func_golbal.py

def func():
	global x
	
	print 'x is',x
	x=2
	print 'Change local x to',x
	
x=50
func()
print 'Value of x is:',x
