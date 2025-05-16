# sum-of-the-digits-of-a-given-number



def sumOfTheDigitOfAGivenNumber (num) :
    sum = 0
    for i in range(0 , len(num)):
        sum += int(num[i])
    return sum



num = input("Enter your NUmber : ")

print("Ths sum of all digits :" , sumOfTheDigitOfAGivenNumber(num))