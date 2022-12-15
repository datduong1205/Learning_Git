word = list("blue") # ['b', 'l', 'u', 'e']
revealword = "****"
UserGuess = "u"

WordList = list(revealword) #['*', '*', '*', '*']
print(WordList)

"""indices = [i for i, letter in enumerate(word) if letter == UserGuess] #[(0, 'b'), (1, 'l'), (2,'u'), (3, 'e')]
print(indices)
print(type(indices))

for index in indices:
    print(type(index))
    WordList[index] = UserGuess
    print(WordList) # ['*', '*', 'u', '*']

revealword = "".join(WordList) # **u*
print(revealword)"""

"""for i in range(10):
    if i % 2 == 0:
        print(i)

i = [i for i in range(10) if i % 2 == 0]"""

