# Name: Dat , ID: 100886108

import time
import random   

try:
    while True:
        correct = 0 
        count = 0
        totalquestion = 5
        StartTime = time.time()
        print("The quiz has started!")
        while count != totalquestion:
            count += 1
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            CorrectAnswer = num1 ** num2
            answer = int(input(f"What is {num1} ** {num2} ? "))
            if answer == CorrectAnswer:
                print("You are correct!")
                correct += 1 
            else:
                print("You are wrong!")
                print(f"Correct answer is: {CorrectAnswer}")
        EndTime = time.time()
        TotalTime = int(EndTime - StartTime)
        print(f"The number of points received are {correct} out of 5 / Total time taken is {TotalTime}")
        NextQuiz = input("Do you want to retake the quiz? Type Y/N: ")
        if NextQuiz == "Y":
            continue 
        elif NextQuiz == "N":
            print("Exit!")
            break
        else:
            print("Invalid Input!")
except ValueError:
    print("Invalid Input!")

