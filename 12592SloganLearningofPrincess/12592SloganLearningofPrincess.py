if __name__ == "__main__":
    princeNum = input("Enter Prince part:")
    i = 0
    n = 0
    slogans = {}
    questions = []
    output = []
    while i < int(princeNum):
        front = input()
        back = input()
        slogans[front] = back
        i+=1
    princessNum = input("Enter Princess part:")
    while n < int(princessNum):
        question = input()
        questions.append(question)
        n+=1
    for index in range(len(questions)):
        output.append(slogans.get(questions[index]))
    for num in range(len(output)):
        print(output[num])
    
    
