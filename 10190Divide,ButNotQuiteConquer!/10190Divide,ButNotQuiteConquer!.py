if __name__ == "__main__":
    num = 0
    result = []
    while num<4:
        s1 = input("Enter number that will be divided:")
        s2 = input("Enter number that will divide the former one:")
        integer = int(s1)
        devide = int(s2)
        output = []
        while 1:
            output.append(integer)
            remainder = integer % devide
            if remainder != 0:
                result.append('Boring!')
                break
            else:
                integer = integer//devide
                if integer == 1:
                    output.append(integer)
                    result.ppend(output)
                    break
        num+=1
    for i in range(len(result)):
        if isinstance(result[i],str):
            print(result[i])
        else:
            print(' '.join(map(str,result[i])))

        

