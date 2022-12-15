from prettytable import PrettyTable
import pandas as pd

def AddAccount(username, password):
    global Usernamelist, Passwordlist, UserInfo
    Usernamelist.append(username)
    Passwordlist.append(password)
    UserInfo[username] = password

def CreateAccount():
    global Usernamelist

    print("\nCreate Acount".rjust(20))
    while True:
        Usernamechoice = input("Username: ")
        if Usernamechoice in Usernamelist:
            print("Username is unavailable. Please re-enter!")
        else:
            print("Username choose successfully!")
            break
    
    while True:
        check = False
        Passwordchoice = input("Password : ")
        num , lower, upper = 0, 0, 0
        for i in Passwordchoice:
            if i.isdigit():
                num += 1
            elif i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            
        if len(Passwordchoice) >= 7 and num >= 1 and lower >= 1 and upper >=1:
                check = True
                
        if check:
            print("Strong Password!")       
            break
        else:
            print("Weak Password! Your password must contain at least 1 lowercase, uppercase, and digit")
    AddAccount(Usernamechoice, Passwordchoice)
    
def AdminLoginPage():
    global Usernamelist, Passwordlist, UserInfo
   
    print()
    print("Admin Login".rjust(20))
    
    while True:
        Options = input("Do you have an account? [y/n]: ").lower()
        if Options == "y":
            while True:
                UsernameEnter = input("Username: ")
                if UsernameEnter in Usernamelist:
                    Passwordenter = input("Password: ")
                    if Passwordenter in Passwordlist and UserInfo[UsernameEnter] == Passwordenter:
                        print("Login successfully!")
                        return True
                    else:
                        print("Wrong password! Please try again")
                else:
                    print("Username does not exist! Please try again")
                
        elif Options == "n":
            CreateAccount()
        else:
            print("Invalid Input! Please try again.")

def StudentDatabase():
    global StudentInfo
    print()
    print("Student Database".rjust(20))
    if StudentInfo == []:
        print("No data available. Please add a student")
        choice = int(input("Enter your choice:\n 1. Main menu\n 2. Exit\n Choose: "))
        if choice == 1:
            HomeInterface()
        elif choice == 2:
            print("Exit!")
            return True
        else:
            print("Invalid Input!")
    else:
        heading = ["DOB:", "Gender:", "Debt:", "Email:", "Emergency Contact:", "Courses:", "Fees:", "Awards & Financial Aid:", "Final Grades:"]
        df = pd.DataFrame(data=StudentInfo, index=heading)
        print(df)
        
def AddStudent():
    global StudentInfo, StudentTable
    
    print()
    print("New Student Details".rjust(20))
    while True:
        print("Enter the following details: ")
        firstname = input("Enter first name: ")
        middlename = input("Enter middle name: ")
        lastname = input("Enter last name: ")
        dob = input("Enter dob: ")
        gender = input("Enter gender: ")
        department = input("Enter department: ")
        email = input("Enter email: ")
        emergencycontact = input("Enter emergency contact details: ")
        coursesopted = input("Courses opted: ")
        fees = input("Information about fees: ")
        awards = input("Awards and financial aid: ")
        finalgrades = input("Final grades: ")
        
        Save = input("Save the details [y/n]: ").lower()
        if Save == "y":
            StudentTable.add_row([firstname, middlename, lastname, dob, gender, department, email, emergencycontact, coursesopted, fees, awards, finalgrades])
            StudentInfo[firstname + middlename + lastname] = dob, gender, department, email, emergencycontact, coursesopted, fees, awards, finalgrades
        NextStudent = input("Add more students [y/n]: ").lower()
        if NextStudent == "n":
            print(StudentTable)
            break

def StudentDetailsTable():
    global StudentTable
    return StudentTable

def HomeInterface():
    print()
    print("Student Ledger".rjust(20))
    while True:
        choice = int(input("Select an option:\n 1. Add a Student\n 2. Display student database\n 3. Search student details\n 4. Exit\n Choose: "))
        if choice == 1:
            AddStudent()
        elif choice == 2:
            if StudentDatabase():
                break
        elif choice == 3:
            print(StudentDetailsTable())
        elif choice == 4:
            print("Program Ends")
            break

StudentInfo = {}
Usernamelist = ["Dat"]
Passwordlist = ["Tran"]
UserInfo = {"Dat": "Tran"}        
if AdminLoginPage():
    StudentTable = PrettyTable(["First Name", "Middle Name", "Last Name", "DOB", "Gender", "Debt", "Email", "Emergency Contact", "Courses", "Fees", "Awards & Financial Aid", "Final Grades"])
    HomeInterface()