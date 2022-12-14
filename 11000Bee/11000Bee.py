output = []
def countNumber(Female,Male,year):
    i = 1
    while 1:
        formerFemale = Female
        formerMale = Male
        Female = formerMale*1 + 1
        Male = formerMale*1 + formerFemale*1
        if i == int(year):
            total = Female+Male
            output.append(str(Male)+" "+str(total))
            break
        i+=1

if __name__ == "__main__":
    while 1:
        year = input("Please Enter The Year:")
        if int(year) == -1:
            break
        else:
            Female = 1
            Male = 0
            if int(year) == 0:
                print("0 1")
            else:
                countNumber(Female,Male,year)
    for i in range(len(output)):
        print(output[i])

