output = []
def caluclatePage(numbers,input):
    total = 0
    for i in range(100000):
        total = total + numbers[i]
        if total >= input:
            if total - input == 0:
                output.append(str(numbers[i+1])+" "+str(i+1))
                break
            else:
                output.append(str(total - input)+" "+str(i))
                break

if __name__ == "__main__":
    numbers = []
    for i in range(100000):
        numbers.append(i)
    while 1:
        input = input("Enter Anita count pages:")
        if int(input) == 0:
            break
        else:
            caluclatePage(numbers,int(input))
    for i in range(len(output)):
        print(output[i])
    
    
    