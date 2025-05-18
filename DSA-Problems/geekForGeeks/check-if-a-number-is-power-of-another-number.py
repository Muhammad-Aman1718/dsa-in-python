# check-if-a-number-is-power-of-another-number

# Given two positive numbers x and y, check if y is a power of x or not.

def checkNumber(n,m):
    if n == 1 :
        return m == 1
    pow = 1
    while pow < m :
        pow *= n          
    return pow == m



num1 = int(input("Enter your number : "))
num2 = int(input("Enter your number : "))

print(checkNumber(num1, num2))