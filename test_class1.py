#Filename:test_class1.py

class PositiveInteger(int):
	def __new__(cls,value):
		return super(PositiveInteger,cls).__new__(cls,abs(value))

i=PositiveInteger(-3)

print i