print('    .')
print('   /|')
print('  / |')
print(' /  |')
print('/___|')

"""				Variables & Datatypes	 		"""

character_name = "Louis" # string
character_age = 50 # interger
is_Male = True # boolean
print("There once was a man named " + character_name + ",")
print("He was " + str(character_age) + " years old.")

character_name = "May"
print("He really liked the name " + character_name + ",")
print("but he didn't like being " + str(character_age) + ".")

print("York\nUniversity")


phrase = "Seneca\\College"
print(phrase + " is cool")

print(phrase.lower().islower())

print(phrase.upper().isupper())

print(len(phrase)) 

print(phrase[0])

print(phrase.index("College"))

print(phrase.replace("College", "University"))

my_num = -5

print(str(my_num) + " is my favorite number")
print(-2.21312)
print(2 + 1.35)
print(2 * 2)
print(4 // 2)
print(3 * (4 + 5))

from math import *  

print(abs(my_num)) 		# giá trị Abs
print(pow(4, 2))		# lũy thừa   
print(max(10, 20))			
print(min(120, 300))
print(round(3.43))		# làm tròn
print(floor(3.7)) 		# làm tròn xuống
print(ceil(3.7))		# làm tròn lên


"""				List			"""

lucky_number = [6,4,2]
Friends = ["Tao Nguyen", ["Bao", "Tran"], 2004, lucky_number]

print(Friends[2])
print(Friends[-1])
print(Friends[1:None])
print(Friends.index(2004))

Friends[3] = 2701
print(Friends)

Friends.extend(lucky_number) # kết hợp 2 list với nhau
print(Friends)

Friends.append("1205")
print(Friends)

Friends.insert(1, "Dat")
print(Friends)

Friends.remove("Dat")
print(Friends)

Friends.pop()
print(Friends)

print(Friends.count("Tao Nguyen"))

lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

Friends2 = Friends.copy()


"""				Tuple			"""

coordinates = [(4, 5), (6, 7), (80, 34)]
# coordinates[1] = 10 error
print(coordinates[1])


"""				Functions			"""
# define
def say_hi(name, age):
	print("Hello " + name + ", you are " + str(age))


print("top")
say_hi("Mike", 18)
say_hi("Steve", 21)

"""				Return Statement			"""

def cube(num):
	return num*num*num


result = cube(4)
print(result)

def answer(career):
	return "Tran is a " + career


print(answer("Lawyer"))

"""				If Statements			"""

is_male = True
is_tall = False

if is_male or is_tall:
	print("You are a male or tall or both")
else:
	print("You neither male nor tall")

if is_male and is_tall:
	print("You're a tall male  ")
elif is_male and not(is_tall):
	print("You are a short male")
elif not(is_male) and is_tall:
	print("You are not a male but are tall")
else:
	print("You are not a male and not tall ")


"""				If Statements & Comparisions		"""

# == : equal
# != : not equal

def max_num(num1, num2, num3):
	if num1 >= num2 and num1 >= num3: 
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else:
		return num3

print(max_num(300,150,4))


"""				Advanced Calculator			"""

# input.py


"""				Dictionaries		"""
# Key must be unique

monthCoversions = {
	"Jan": "January",
	"Feb": "February",
	"Mar": "March",
	"Apr": "April",
	"May": "May",
	"Jun": "June",
	"Jul": "July",
	"Aug": "August",
	"Sep": "September",
	"Oct": "October",
	"Nov": "November",
	"Dec": "December",
}

print(monthCoversions)

print(monthCoversions["Nov"])

print(monthCoversions.get("Dec"))

print(monthCoversions.get("Luv", "BaoTran"))

"""				While Loop			"""

i = 1

while i <= 10:
	print(i)
	i = i + 1

print("Done with loop")


"""				Guessing Game		"""
'''
Lover = "Who is my Lover ? "
print(Lover)

secret_word = "BaoTran"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Enter guess:")
		guess_count += 1 
	else:
		out_of_guesses = True


if out_of_guesses:
	print("Out of guesses, YOU LOSE!")
else:
	print("YOU WIN!")
'''

"""				For  Loop			"""

for letter in "York University":
	print(letter)

friends = ["Alexa", "Siri", "Google"]

for friend in friends:
	print(friend)


for count in range(len(friends)):
	print(count)

for INDEX in range(5):
	if INDEX == 0:
		print("First Iteration")
	else:
		print("Not First")


"""				Exponent Function			"""

print(2**4)

def raise_to_power(base_num, pow_num):
	result = 1
	for Index in range(pow_num):
		result = result * base_num
	return result

print(raise_to_power(3, 4))

"""				2D Lists & Nested Loops			"""

number_grid = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[0]
]

print(number_grid[2][1])

for row in number_grid:
	for column in row:
		print(column)



"""				Build a Translator			"""

'''
def translate(Phrase):
	translation = ""
	for letter in Phrase:
		if letter.lower() in "aeiou":
			if letter.isupper():
				translation = translation + "G"
			else:
				translation = translation + "g"

		else:
			translation = translation + letter 
	return translation

print(translate(input("Enter a phrase: ")))
'''

"""				Comments			"""

# ''' ''' """ """

"""				Try / Except			"""


try: 
	value = 10/0
	Number = int(input("Enter a number: "))
	print(Number)
except ZeroDivisionError as err:
	print(err)
except ValueError:
	print("Invalid Input")


"""				Reading Files			"""
# "r"  : read
# "w"  : write  (overwriting everything in file)
# "a"  : append (add text at the end of file)
# "r+" : read & write 


employee_file = open("employee.txt", "r")

print(employee_file.readable())

# .read : spit out all information in the file

# .readline : read first line in file
print(employee_file.readline())

print(employee_file.readline())

# .readlines : put all information into a list
for employee in employee_file.readlines():
	print(employee)


employee_file.close()


"""				Writing to Files			"""

'''
employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()
'''

"""				Modules and Pip				"""

import usefull_tools

print(usefull_tools.roll_dice(10))

"""				Classes & Objects				"""

from Student import Student

student1 = Student("Jim", "Business", 3.8, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student1.gpa)

print(student2.major)
print(student2.is_on_probation)

"""				Building a Multiple Choice Quiz					"""

"""				Object Functions				"""

print(student1.on_honor_roll())
print(student2.on_honor_roll())

"""				Inheritance				"""

from Chef import Chef

myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

print("\n")

from Chef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()

"""				Python Interpreter				"""




