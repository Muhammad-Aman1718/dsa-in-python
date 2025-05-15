# sum-of-squares-of-first-n-natural-numbers

def sumSquareFirstNaturalNumber(num):
    sumOFAllNumbers = 0
    for n in range(1, num +1):
        sumOFAllNumbers +=  n ** 2
    return sumOFAllNumbers



num  = int(input("Enter your number : "))

print(sumSquareFirstNaturalNumber(num))