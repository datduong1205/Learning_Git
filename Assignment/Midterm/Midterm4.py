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

#Name: Dat, ID: 100886108, Question 3

def calc_average(mark1, mark2, mark3, mark4, mark5):
    AverageoftheMarks = (mark1 + mark2 + mark3 + mark4 + mark5)/5
    return AverageoftheMarks

def determine_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 80 and mark <= 89:
        return "B"
    elif mark >= 70 and mark <= 79:
        return "C"
    elif mark >= 60 and mark <= 69:
        return "D"
    elif mark < 60:
        return "F"

mark1, mark2, mark3, mark4, mark5 = map(int, input("Enter 5 test marks: ").split())

AverageMark = print("Your average test marks is:", calc_average(mark1, mark2, mark3, mark4, mark5))

print("Your letter grade for the first mark is:", *determine_grade(mark1))
print("Your letter grade for the second mark is:", *determine_grade(mark2))
print("Your letter grade for the third mark is:", *determine_grade(mark3))
print("Your letter grade for the fourth mark is:", *determine_grade(mark4))
print("Your letter grade for the fifth mark is:", *determine_grade(mark5))
