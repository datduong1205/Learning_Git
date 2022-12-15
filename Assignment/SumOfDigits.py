n = int(input("Enter a number between 0 and 1000: "))

Sum = 0
while n > 0:
    LastDigit = n % 10
    n = n // 10
    Sum += LastDigit

print("The sum of the digits:", Sum)
