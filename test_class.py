#Filename:test_class.py

class PositiveInteger(int):
	def __init__(self,value):
		super(PositiveInteger,self).__init__(self,abs(value))

i=PositiveInteger(-3)

print i