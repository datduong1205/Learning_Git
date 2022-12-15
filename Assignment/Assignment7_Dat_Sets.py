# Name: Dat , ID: 100886108

#Program1: sets.py

def checkvowelsConsonants(sentence):
    vowels = set("AEIOUaeiou")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    countvowels = 0
    countconsonants = 0
    for i in sentence:
        if i in vowels:
            countvowels += 1
        elif i in consonants:
            countconsonants += 1
        else:
            continue
    return countvowels, countconsonants

sentence = list(input("Please enter a sentence (must contain special characters): "))

while True:
    UserChoice = int(input("Options:\n 1. Print the number of vowels and consonants\n 2. Exit the program\n Choice: "))
    if UserChoice == 1:
        NumberofVowels, NumberofConsonants = checkvowelsConsonants(sentence)
        print(f"The number of vowels is {NumberofVowels} and the number of consonants is {NumberofConsonants}.\n")
    elif UserChoice == 2:
        print("Program Ends")
        break
    else:
        print("Invalid Input! [1 or 2]")
