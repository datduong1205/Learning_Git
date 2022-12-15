from prettytable import PrettyTable
StudentTable = PrettyTable(["Student#"])
print(StudentTable)

a = 2
StudentTable.add_row(["wow"])
StudentTable.add_autoindex("Student12")
print(StudentTable)