#Filename:inherit.py

class SchoolMenmber():
	'''Represents any school member.'''
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print '(Initialized SchoolMenmber: %s)' %self.name
		
	def tell(self):
		'''Tell my details.'''
		print 'Name: %s,Age: %d'%(self.name,self.age)

class Teacher(SchoolMenmber):
	'''Represents a teacher.'''
	def __init__(self,name,age,salary):
		SchoolMenmber.__init__(self,name,age)
		self.salary=salary
		print '(Initialized Teacher: %s)'%self.name
		
	def tell(self):
		SchoolMenmber.tell(self)
		print 'Salary: %d' %self.salary
	
class Student(SchoolMenmber):
	'''Represents a student.'''
	def __init__(self,name,age,marks):
		SchoolMenmber.__init__(self,name,age)
		self.marks=marks
	
	def tell(self):
		SchoolMenmber.tell(self)
		print 'Maeks: %d' %self.marks
		
t=Teacher('Mrs.Shrividya',40,30000)
s=Student('Swaroop',22,75)

print #prints a blank line

members=[t,s]
for member in members:
	member.tell() #works for both Teacher and Students