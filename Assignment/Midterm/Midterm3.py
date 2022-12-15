"""
Statement of Commitment to Academic Integrity 
As  a  member  of  the  Ontario  Tech  University  community,  I  share  our  community's 
commitment  to  the  highest  standards  of  academic  integrity  and  excellence  in  all 
dimensions of our work.  
I therefore promise that I will not lie, cheat, or use any unauthorized aids or assistance to 
complete any of my essays, assignments, and exams. I further promise that I will not offer 
any unauthorized assistance to any of my fellow students, and I promise that I will not ask 
any of my fellow students for unauthorized assistance. I promise that the work I submit is 
my  own  and  that  where  I  have  drawn  on  the  work  of  others,  I  have  included  proper 
attribution for my sources.
"""

#Name: Dat, ID: 100886108, Question 7 and Question 7 Bonus

import random   

try:
    while True:
        check = True
        print("The quiz has started!")
        RandomNum = int(random.randint(1, 100))
        count = 0
        while check:
            answer = int(input("Guess the correct answer from 1 to 100?: "))
            if answer == RandomNum:
                print("You are correct!")
                print("You've guessed {} times".format(count))
                check = False
            elif answer > RandomNum:
                print("The guess is too high, try again!")
                count += 1
            elif answer < RandomNum:
                print("The guess is too low, try again!")
                count += 1

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