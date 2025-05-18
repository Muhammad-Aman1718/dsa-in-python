#  Prime number



def primeNum(n):
    if 1 >= n:
        return False

    for i in range(2 , n):
        if n % i == 0 :
            return False
    return True


num = int(input("Enter your number : "))

print(primeNum(num))