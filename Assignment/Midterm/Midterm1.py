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

#Name: Dat, ID: 100886108, Question 2 

def FinanceAssistance(AnnualIncome, Children):
    if AnnualIncome >= 30000 and AnnualIncome <= 40000 and Children >= 3:
        AmountOfAssistance = "You recieve:", "$",Children * 1000
        return AmountOfAssistance
    elif AnnualIncome >= 20000 and AnnualIncome <= 30000 and Children >= 2:
        AmountOfAssistance = "You recieve:", "$",Children * 1500
        return AmountOfAssistance
    elif AnnualIncome <= 20000:
        AmountOfAssistance = "You recieve:", "$",Children * 1000
        return AmountOfAssistance

try:
    FamilyIncome = int(input("Please enter your family income: "))
    NumberofChildren = int(input("Please enter the number of children in your family: "))
except ValueError:
    print("Invalid Input!")

print(*FinanceAssistance(FamilyIncome, NumberofChildren))

