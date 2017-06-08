#Filename:func_key.py
def func(a,b=5,c=10):
	print 'a is',a,'and b is',b,'and c is',c

func(10,20)
func(10,c=30)
func(c=20,a=30)