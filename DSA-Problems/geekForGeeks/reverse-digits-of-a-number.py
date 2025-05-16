# reverse-digits-of-a-number


def reverseDigitOfANumber(num) :
    reverseNum = ""
    for i in range(len(num) - 1 , -1 , -1):
        reverseNum += num[i]
    return reverseNum





num =  input("Enter your number : ")
print(reverseDigitOfANumber(num))