if __name__ == "__main__":
    princeNum = input("Enter Prince part:")
    i = 0
    n = 0
    slogans = {}
    questions = {}
    while i < int(princeNum):
        front = input()
        back = input()
        slogans[front] = back
        #print(slogans)
        i+=1
    princessNum = input("Enter Pricess part:")
    while n < int(princessNum):
        question = input()
        questions[question] = ""
        print(questions)
        n+=1
    
    
