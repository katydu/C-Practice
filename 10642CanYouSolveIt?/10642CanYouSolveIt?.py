if __name__ == "__main__":
    output = []
    cases_input = input("Enter number of test cases:")
    cases = int(cases_input)
    for i in range(1,1):
        print(i)
    while int(cases)>0:
        count = 0
        coordinate = input("Enter Coordinates:").split()
        Sx = int(coordinate[0])
        Sy = int(coordinate[1])
        Ex = int(coordinate[2])
        Ey = int(coordinate[3])
        start = Sx+Sy+1
        end = Ex+Ey
        for i in range(int(start), int(end)):
            count = count + i + 1
        count = count+Sy+Ex+1
        output.append(count)
        cases -=1
    for i in range(len(output)):
        print("Case "+str(i+1)+": "+str(output[i]))

