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

#Name: Dat, ID: 100886108, Question 4

try:
    ClassA = int(input("How many tickets have class A been sold ?: "))
    ClassB = int(input("How many tickets have class B been sold ?: "))
    ClassC = int(input("How many tickets have class C been sold ?: "))
except ValueError:
    print("Invalid Input!")

ClassAIncome = ClassA * 25
ClassBIncome = ClassB * 20
ClassCIncome = ClassC * 15

TotalIncome = ClassAIncome + ClassBIncome + ClassCIncome 
print("Total income produced from all sales: " + "$" + str(TotalIncome))