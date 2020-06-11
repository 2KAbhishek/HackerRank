import functools
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        average = functools.reduce(lambda a,b: a+b, scores) / len(scores)
        if (average < 40):
            return 'T'
        elif ((average >= 40) and (average < 55)):
            return 'D' 
        elif ((average >= 55) and (average < 70)):
            return 'P'
        elif ((average >= 70) and (average < 80)):
            return 'A'
        elif ((average >= 80) and (average < 90)):
            return 'E'
        elif ((average >= 90) and (average <= 100)):
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
