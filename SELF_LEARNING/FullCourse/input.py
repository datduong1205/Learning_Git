# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)

'''color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
name = input("Enter a name: ")

print("Rose are " + color)
print(plural_noun +  " are blue")
print("I Love " + name)
'''



"""				Advanced Calculator			"""

'''num1 = float(input("Enter first number: "))
op = input("Enter first operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
	print(num1 + num2)
elif op == "-":
	print(num1 - num2)
elif op == "/":
	print(num1 / num2)
elif op == "*":
	print(num1 * num2)
else:
	print("Invalid operator")
'''

"""				Guessing Game		"""

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
	print("Out of gueesses, YOU LOSE!")
else:
	print("YOU WIN!")







