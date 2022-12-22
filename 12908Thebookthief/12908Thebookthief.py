output = []
def caluclatePage(numbers,count):
    total = 0
    for i in range(100000):
        total = total + numbers[i]
        if total >= count:
            if total - count == 0:
                output.append(str(numbers[i+1])+" "+str(i+1))
                break
            else:
                output.append(str(total - count)+" "+str(i))
                break

if __name__ == "__main__":
    numbers = []
    for i in range(100000):
        numbers.append(i)
    while 1:
        count = input("Enter Anita count pages:")
        if int(count) == 0:
            break
        else:
            caluclatePage(numbers,int(count))
    for i in range(len(output)):
        print(output[i])
    
    
    