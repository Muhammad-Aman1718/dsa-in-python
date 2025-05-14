# 8. Create a program that checks if a given string is a palindrome.

# word = input("Enter your word : ")
# isPalidrome = True

# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - i - 1]:
#         isPalidrome = False
#     break

# if isPalidrome:
#     print("This is palidrome")
# else:
#     print("this is not ")

#  Create a program that checks if a given number is prime or not.


# num = int(input("Enter your number : "))

# if num < 2:
#     print(f" {num} this number is not prime ")
# else:
#     isPrime = True
#     for i in range(2, int(num**0.5)):
#         if num % i == 0:
#             isPrime = False
#             break


# if isPrime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# tableNum = int(input("Enter your number : "))
# tableRange = int(input("Enter your range : "))

# for i in range(1, tableRange + 1):
#     result = tableNum * i
#     print(f"{tableNum} x {i} = {result} ")



#  Factorial 

num = int(input("Enter your number : "))
factorial = 1

for i in range( 1,num + 1 ):
    factorial *= i


# print(factorial, "this is factorial ")

