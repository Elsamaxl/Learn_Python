#Filename:lambda.py

def make_reeater(n):
	return lambda s:s*n
	
twice=make_reeater(2)

print twice('world')
print twice(5)