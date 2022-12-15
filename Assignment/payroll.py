name = input("Enter employee's name: ")
HoursWorkedaWeek = int(input("Enter number of hours worked in a week: "))
HourlyPayRate = float(input("Enter hourly pay rate: "))
ftwhr = float(input("Enter federal tax withholding rate: "))
stwhr = float(input("Enter state tax withholding rate: "))

GrossPay = HoursWorkedaWeek * HourlyPayRate
ftwh = GrossPay * ftwhr
stwh = GrossPay * stwhr
TotalTaxes = ftwh + stwh
NetPay = GrossPay - TotalTaxes
print("#################################")

print("\n\nEmployee Name:",name)
print("Hours Worked:", HoursWorkedaWeek)
print("Pay Rate: $"+ str(HourlyPayRate))
print("Gorss pay: $" + str(GrossPay))
print("Deductions:")
print(" Federal Withholding (" +  str(ftwhr*100) + "%): $" +  str(ftwh))
print(" State Withholding (" +  str(stwhr*100) + "%): $" + str(stwh))
print(" Total Deduction: %" + str(TotalTaxes))
print("Net Pay: $" + str(NetPay))