from datetime import datetime

if __name__ == "__main__":
    times = input("Enter how many times needs to be calculated:")
    output = []
    i = 1
    while i <= int(times) :
        CurrentDate = input("Enter CurrentDate:")
        CurrentDate = datetime.strptime(CurrentDate, "%d/%m/%Y")
        BirthDay = input("Enter BirthDay:")
        BirthDay = datetime.strptime(BirthDay, "%d/%m/%Y")
        age = CurrentDate - BirthDay
        print("age:"+str(age.days))
        if age.days == 0:
            output.append("0")
        elif age.days < 0:
            output.append("Invalid birth date")
        elif age.days/365 >130:
            output.append("Check birth date")
        else:
            output.append(str(age.days//365))
        i = i + 1
    for i in range(len(output)):
        print("Case #" + str(i+1) + ": " + output[i])
