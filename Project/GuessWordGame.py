import random

FourLengthWord = ["blue", "moon", "snow"]
FiveLengthWord = ["hello", "table", "mouse", "about"]

def WordtoGuess(length):
    if length == 4:
        word = random.choice(FourLengthWord).lower()
    elif length == 5:
        word = random.choice(FiveLengthWord).lower()
    return word

def Game(word, attempts):
    revealword = "*" * len(word)
    PreviousGuess = "" 
    WrongGuesses = []
    print("Word:", revealword)
    while attempts != 0:
        print("Guess remaining: ", attempts)
        print("Previous Guess: ", PreviousGuess)
        UserGuess = input("Choose a letter to guess: ").lower()
        PreviousGuess = UserGuess
        attempts -= 1

        if UserGuess in word:
            WordList = list(revealword)
            indices = [i for i, letter in enumerate(word) if letter == UserGuess]
            for index in indices:
                WordList[index] = UserGuess
            revealword = "".join(WordList)
            print(f"{UserGuess} is in the word!\n")
            print("Word:", revealword)

        elif UserGuess == "exit" or UserGuess == "stop":
            print("Game End!")
            break

        elif UserGuess in WrongGuesses:
            print("\n{} is not present in the word and has been guessed before. Please enter another letter".format(UserGuess))
            print("Word:", revealword)
            
        else:
            print(f"{UserGuess} is not in the word! Try again!\n")
            print("Word:", revealword)
            WrongGuesses.append(UserGuess)
        
        if revealword == word:
            print("Congratulations! You Win")
            break
    
    else:
        print("No more guesses left! You lose")


def NextGame():
    a = input("Do you want to continue? (Y/N):")
    if a == "Y":
        return True
    elif a == "N":
        print("End Game")
        return False


while True:
    print("Welcome to the Guess-the-letters Game!\n")
    CheckAttempt = True
    CheckWordLength = True
    while CheckAttempt:
        attempts = input("How many guesses you want [1-10]: ")
        if attempts.isnumeric():
            attempts = int(attempts)
            if attempts > 10:
                print("Enter a number within range provided!")
                continue 
            else:
                CheckAttempt = False
        else:
            print("Invalid input! Please enter a number within range provided")
    
    while CheckWordLength:
        WordLength = input("Select a word length [4-5]: ")
        if WordLength.isnumeric():
            WordLength = int(WordLength)
            if WordLength not in range(4, 6):
                print("Enter a number within range provided!")
                continue 
            else:
                CheckWordLength = False
        else:
            print("Invalid input! Please enter a number within range provided")    
    
    print("Selecting the word…\n")
    
    word = WordtoGuess(WordLength)

    Game(word, attempts)

    if NextGame():
        continue        
    else:
        break


        


    



    

