if __name__ == "__main__":
    totalCent = input("Please Enter Total Cent:")
    total = int(totalCent)
    count = 0
    c = 0
    OriginalCent = [50,25,10,5,1]
    Cent = OriginalCent
    for m in range(len(Cent)):
        if Cent[m] > total:
            Cent[m] = 0
            c = c+1
    for o in range(c):
        Cent.pop(0)
    for n in range(len(Cent)):
        print("n現在是："+str(n))
        for i in range(len(Cent)):
            print(Cent)
            print("i現在是："+str(i))
            if Cent[i] > total:
                continue
            else:
                print("pretotal:"+str(total))
                total = total//Cent[i]
                print("total:"+str(total))
                total = int(totalCent)
                remainder = total%Cent[i]
                print("remainder:"+str(remainder))
                if remainder == 0:
                    count = count + 1
                    print("count:"+str(count))
                    break
        Cent.pop(0)
        total = int(totalCent)
    print(count)
    
    