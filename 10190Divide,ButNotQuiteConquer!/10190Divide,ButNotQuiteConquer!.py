if __name__ == "__main__":
    num = 0
    result = []
    while num<4:
        s = input().split()
        s1 = s[0]
        s2 = s[1]
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
                    result.append(output)
                    break
        num+=1
    for i in range(len(result)):
        # if output is Boring!
        if isinstance(result[i],str):
            print(result[i])
        # if output is array
        else:
            print(' '.join(map(str,result[i])))

        

