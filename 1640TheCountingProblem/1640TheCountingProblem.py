def countAllNumber(first,end,step):
    string = ""
    for i in range(int(first),int(end)+1,step):
        string = string + str(i)
    return string

if __name__ == "__main__":
    output = []
    while 1:
        digitsNum = [0]*10
        numbers = ""
        integer = input().split()
        first = integer[0]
        end = integer[1]
        if int(first) == 0 & int(end) == 0:
            break
        else:
            if int(first) > int(end):
                numbers = countAllNumber(first, end, -1)
            else:
                numbers = countAllNumber(first, end, 1)
            # calulate each digits's quantity in numbers
            for i in range(len(numbers)):
                digitsNum[int(numbers[i])]+= 1
            output.append(digitsNum)
    for i in range(len(output)):
        print(' '.join(map(str,output[i])))
            
            

