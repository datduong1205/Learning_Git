word = list("moon") # ['b', 'l', 'u', 'e']
revealword = "****"

while True:
    UserGuess = input("Choose a letter to guess: ")
    if UserGuess in word:
        revealwordlist = list(revealword)
        index = word.index(UserGuess)
        revealwordlist[index] = UserGuess
        revealword = "".join(revealwordlist)
        print(revealword)
    else:
        print("Try again!")