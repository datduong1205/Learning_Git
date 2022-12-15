minutes = int(input("Enter the number of minutes: "))
years = minutes // 525600
days = (minutes - (years * 525600)) // 1440  

print("{} minutes os approximately {} years and {} days".format(minutes, years, days))
