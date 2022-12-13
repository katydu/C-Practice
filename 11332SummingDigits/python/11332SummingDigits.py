def calculateDigit(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10) 
        # using '//' rather than '/' to divided with no remain
        num = num//10
    if sum < 10:
        return sum
    else:
        return calculateDigit(int(sum))

if __name__ == "__main__":
    inputArray = []
    while(1):
        num = input("please enter the number : ")
        if int(num) == 0:
            break
        else:
            inputArray.append(calculateDigit(int(num)))
    for i in range(len(inputArray)):
        print(inputArray[i])