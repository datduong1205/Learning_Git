class Complex: 
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def add(self, number):
		real = self.real + number.real
		imaginary = self.imaginary + number.imaginary
		result = Complex(real, imaginary)
		return result


n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)
print("real = ", result.real)
print("imaginary = ", result.imaginary)



class Student:
	def __init__(self, name, age, MathScore, LiteraturScore):
		self.name = name
		self.age = age
		self.MathScore = MathScore
		self.LiteraturScore = LiteraturScore 
		self.Teacher = "Dat"

	def average_score(self):
		AveScore = (self.MathScore + self.LiteraturScore)/2
		return AveScore

	def print_info(self):
		print("Student name {} studies with {}: \nAverage Score: {}".format(self.name, self.Teacher, self.average_score()))


students = []

s1 = Student("David", 21, 9, 7)
s2 = Student("Bob", 19, 5, 6)
s3 = Student("Janet", 29, 10, 6)

s2.Teacher = "Jane"

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()
