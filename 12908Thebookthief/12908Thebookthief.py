output = []
def caluclatePage(numbers,AnitaCountPages):
    total = 0
    for i in range(100000):
        total = total + numbers[i]
        if total >= AnitaCountPages:
            if total - AnitaCountPages == 0:
                output.append(str(numbers[i+1])+" "+str(i+2))
                break
            else:
                output.append(str(total - AnitaCountPages)+" "+str(i+1))
                break

if __name__ == "__main__":
    numbers = []
    for i in range(1,100001):
        numbers.append(i)
    print(numbers[0])
    while 1:
        AnitaCountPages = input("Enter Anita count pages:")
        if int(AnitaCountPages) == 0:
            break
        else:
            caluclatePage(numbers,int(AnitaCountPages))
    for i in range(len(output)):
        print(output[i])
    
    
    